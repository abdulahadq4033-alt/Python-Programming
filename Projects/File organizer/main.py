import os
import shutil

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".c", ".cpp", ".java"]
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    # Create folders
    for category in FILE_CATEGORIES.keys():
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # Move files
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(directory, category, filename))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(directory, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))

    print("Files organized successfully!")

# Run program
path = input("Enter folder path: ")
organize_files(path)
