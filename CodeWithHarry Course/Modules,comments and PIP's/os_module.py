# Import the os module
import os

# Specify the directory path (change this to any directory you want)
directory_path = "."

# Get a list of directory contents
contents = os.listdir(directory_path)

# Print the list of contents
print("Contents of the directory:", contents)

"""This program lists all files and directories in the specified path using the os module."""