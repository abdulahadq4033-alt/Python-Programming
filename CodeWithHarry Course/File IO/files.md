"""
===========================
FILE INPUT / OUTPUT IN PYTHON
===========================

File I/O (Input/Output) in Python is used to:
- Read data from a file
- Write data to a file
- Append new data to an existing file

Python provides built-in functions to handle files easily.
"""

# -----------------------------------------
# 1. OPENING A FILE
# -----------------------------------------
"""
To work with a file, we first open it using the open() function.

Syntax:
file_object = open("filename", "mode")

Modes:
'r'  -> Read (default mode)
'w'  -> Write (creates new file / overwrites existing file)
'a'  -> Append (adds data to the end of file)
'x'  -> Create (fails if file already exists)
'b'  -> Binary mode
't'  -> Text mode (default)
"""

# Example: Opening a file in write mode
file = open("example.txt", "w")

# -----------------------------------------
# 2. WRITING TO A FILE
# -----------------------------------------
"""
The write() method is used to write text into a file.
If the file does not exist, it will be created.
If it exists, its content will be overwritten (in 'w' mode).
"""

file.write("Hello, this is an example of File I/O in Python.\n")
file.write("This text is written using write() method.\n")

# Always close the file after use
file.close()

# -----------------------------------------
# 3. APPENDING TO A FILE
# -----------------------------------------
"""
Append mode ('a') adds new content to the end of the file
without deleting existing content.
"""

file = open("example.txt", "a")
file.write("This line is appended to the file.\n")
file.close()

# -----------------------------------------
# 4. READING FROM A FILE
# -----------------------------------------
"""
To read a file, we open it in read mode ('r').

Methods:
read()      -> Reads entire file
readline()  -> Reads one line
readlines() -> Reads all lines as a list
"""

file = open("example.txt", "r")
content = file.read()
file.close()

print("File Content:\n")
print(content)

# -----------------------------------------
# 5. USING 'with' STATEMENT (BEST PRACTICE)
# -----------------------------------------
"""
The 'with' statement automatically closes the file.
This is the recommended way to work with files.
"""

with open("example.txt", "r") as file:
    content = file.read()
    print("Reading using with statement:\n")
    print(content)

# -----------------------------------------
# 6. CHECKING FILE EXISTENCE (OPTIONAL)
# -----------------------------------------
"""
We can check whether a file exists using the os module.
"""

import os

if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")

# -----------------------------------------
# 7. SUMMARY
# -----------------------------------------
"""
- open() is used to open a file
- write() is used to write data
- read() is used to read data
- close() closes the file
- 'with' statement is the safest way to handle files

File I/O is very important for:
- Saving program output
- Reading large data
- Logging
- Configuration files
"""

print("File I/O explanation program completed.")
