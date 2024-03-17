import os

# Get the current directory
current_directory = os.getcwd()

# Navigate to the parent directory
parent_directory = os.path.dirname(current_directory)

# Repeat until the "src" directory is found
while "src" not in os.listdir(parent_directory):
    parent_directory = os.path.dirname(parent_directory)

print("Parent directory of 'src':", parent_directory)
