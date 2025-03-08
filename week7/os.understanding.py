import os
import shutil

# 1. List only directories, files, and all contents in a specified path
def list_contents(pp2-2025):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All:", os.listdir(path))

# 2. Check access to a specified path
def check_access(path):
    print(f"Path Exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

# 3. Test whether a given path exists and find its filename & directory portion
def path_details(path):
    if os.path.exists(path):
        print("Directory portion:", os.path.dirname(path))
        print("Filename portion:", os.path.basename(path))
    else:
        print("Path does not exist.")

# 4. Count the number of lines in a text file
def count_lines(filename):
    try:
        with open(filename, 'r') as f:
            print("Number of lines:", sum(1 for _ in f))
    except FileNotFoundError:
        print("File not found.")

# 5. Write a list to a file
def write_list_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(str(item) + '\n')

# 6. Generate 26 text files named A.txt, B.txt, ..., Z.txt
def generate_text_files():
    for i in range(65, 91):  # ASCII values for A-Z
        with open(chr(i) + ".txt", 'w') as f:
            f.write(f"This is {chr(i)}.txt file")

# 7. Copy contents of one file to another
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")

# 8. Delete a file by specified path (check access and existence first)
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted successfully.")
        else:
            print("No write permission to delete the file.")
    else:
        print("File does not exist.")
