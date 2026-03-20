import os
import random
import string
import zipfile

# Folder to store generated files
OUTPUT_FOLDER = "random_files"

# File categories and extensions
FILE_TYPES = {
    "videos": [".mp4", ".avi", ".mkv"],
    "images": [".jpg", ".png", ".gif"],
    "documents": [".txt", ".pdf", ".docx"],
    "music": [".mp3", ".wav"],
    "archives": [".zip"],
    "code": [".py", ".c", ".js", ".html"]
}

# Create folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Generate random filename
def random_name(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Generate random content
def random_content(size=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

# Create dummy file
def create_file(filepath, size=100):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(random_content(size))

# Create fake zip archive
def create_zip(filepath):
    with zipfile.ZipFile(filepath, 'w') as zipf:
        temp_file = "temp.txt"
        with open(temp_file, "w") as f:
            f.write(random_content(50))
        zipf.write(temp_file)
        os.remove(temp_file)

# Number of files to generate
NUM_FILES = 30

# Flatten all extensions into one list
all_extensions = []
for category in FILE_TYPES.values():
    all_extensions.extend(category)

# Random file creation
for _ in range(NUM_FILES):
    ext = random.choice(all_extensions)
    name = random_name()
    filepath = os.path.join(OUTPUT_FOLDER, name + ext)

    if ext == ".zip":
        create_zip(filepath)
    else:
        create_file(filepath, random.randint(50, 500))

print(f"{NUM_FILES} random files created in '{OUTPUT_FOLDER}' folder!")