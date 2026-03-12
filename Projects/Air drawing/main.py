import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision
import urllib.request
import os
# pip install opencv-python numpy mediapipe
# -------------------- Download model if needed --------------------
MODEL_PATH = "hand_landmarker.task"
if not os.path.exists(MODEL_PATH):
    print("Downloading hand landmark model (~8MB)...")
    url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task"
    urllib.request.urlretrieve(url, MODEL_PATH)
    print("Model downloaded.")

# -------------------- Setup --------------------
base_options = mp_python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7,
    min_tracking_confidence=0.7
)
detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

canvas = None
prev_point = None
draw_color = (0, 255, 0)
thickness = 4

# Hand landmark indices
INDEX_TIP, INDEX_PIP = 8, 6
MIDDLE_TIP, MIDDLE_PIP = 12, 10

# Connections to draw skeleton
HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),(0,17)
]

def draw_skeleton(frame, landmarks, w, h):
    pts = [(int(lm.x * w), int(lm.y * h)) for lm in landmarks]
    for a, b in HAND_CONNECTIONS:
        cv2.line(frame, pts[a], pts[b], (80, 80, 80), 1)
    for pt in pts:
        cv2.circle(frame, pt, 3, (180, 180, 180), -1)

def finger_up(landmarks, tip_id, pip_id, h):
    return (landmarks[tip_id].y * h) < (landmarks[pip_id].y * h)

print("Controls:")
print("  Index finger only -> Draw")
print("  Two fingers up    -> Pen lifted")
print("  q=quit | c=clear | r/g/b/w/y=color")

# -------------------- Main Loop --------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]

    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert to MediaPipe image
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    result = detector.detect(mp_image)

    mode_text = "No hand"
    current_point = None

    if result.hand_landmarks:
        lm = result.hand_landmarks[0]

        index_up = finger_up(lm, INDEX_TIP, INDEX_PIP, h)
        middle_up = finger_up(lm, MIDDLE_TIP, MIDDLE_PIP, h)

        cx = int(lm[INDEX_TIP].x * w)
        cy = int(lm[INDEX_TIP].y * h)

        if index_up and not middle_up:
            # DRAW MODE
            mode_text = "Drawing"
            current_point = (cx, cy)
            if prev_point is not None:
                cv2.line(canvas, prev_point, current_point, draw_color, thickness)
            cv2.circle(frame, current_point, 10, draw_color, -1)
            cv2.circle(frame, current_point, 14, (255, 255, 255), 2)

        elif index_up and middle_up:
            # PEN LIFTED
            mode_text = "Pen Lifted"
            cv2.circle(frame, (cx, cy), 10, (100, 100, 255), -1)

        else:
            mode_text = "Fist"

        prev_point = current_point if (index_up and not middle_up) else None
        draw_skeleton(frame, lm, w, h)

    else:
        prev_point = None

    # Blend canvas onto frame
    output = cv2.addWeighted(frame, 0.7, canvas, 1.0, 0)

    # UI bar
    color_name = {
        (0,255,0): "GREEN", (0,0,255): "RED",
        (255,0,0): "BLUE", (255,255,255): "WHITE", (0,255,255): "YELLOW"
    }.get(draw_color, "CUSTOM")

    cv2.rectangle(output, (0, 0), (w, 58), (15, 15, 15), -1)
    cv2.putText(output, f"Mode: {mode_text}", (10, 22),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (220, 220, 220), 1)
    cv2.putText(output, f"Color: {color_name}  |  q=quit  c=clear  r/g/b/w/y=color",
                (10, 46), cv2.FONT_HERSHEY_SIMPLEX, 0.52, draw_color, 1)

    cv2.imshow("Air Drawing", output)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros_like(frame)
        prev_point = None
    elif key == ord('r'):
        draw_color = (0, 0, 255)
    elif key == ord('g'):
        draw_color = (0, 255, 0)
    elif key == ord('b'):
        draw_color = (255, 0, 0)
    elif key == ord('w'):
        draw_color = (255, 255, 255)
    elif key == ord('y'):
        draw_color = (0, 255, 255)

# -------------------- Cleanup --------------------
cap.release()
detector.close()
cv2.destroyAllWindows()