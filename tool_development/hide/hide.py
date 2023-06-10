import os

file_path = 'hide.txt'
new_file_path = '.hide.txt'

try:
    os.rename(file_path, new_file_path)
    print(f"File {file_path} has been hidden.")
except FileNotFoundError:
    print(f"File {file_path} has not been hidden.")
except OSError as e:
    print(f"An error occurred while hiding the file: {e}")
