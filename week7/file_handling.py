#There are four different methods (modes) for opening a file:

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""

"""
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""

#The open() function takes two parameters; filename, and mode.

#f = open("demofile.txt")

f = open("myfile.txt", "w")
f.write("Now the file has new content!")
f.close()

f = open("myfile.txt", "r")
print(f.read())
f.close()

#To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("myfile.txt")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
  print("it was just deleted")
else:
  print("The file does not exist")
  
#To delete an entire folder, use the os.rmdir() method

#tasks

import os

#1st
def list_contents(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files

path = "."
dirs, files = list_contents(path)

print("Directories: ", dirs)
print("Files: ", files)
print("All: ", dirs + files)

#2nd
def check_path_access(path):
    print("Checking access for: ", path)
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

path = "test doc.txt"
check_path_access(path)

#3rd
def check(path):
    if os.path.exists(path):
        print("The path ", path, "exists")
        print("Dir: ", os.path.dirname(path))
        print("File: ", os.path.basename(path))
    else:
        print("The path ", path, "doesn't exist")

path = "test doc.txt"
check(path)

#4th
path = "test doc.txt"
print("Number of lines: ", len(open(path).readlines()))

#5th
def write(path, data):
    with open(path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

lst = ["You", "Know", "Who"]
path = "test doc2.txt"
write(path, lst)

#6th
for i in range(0, 26):
    file = f"{chr(ord('a')+i)}.txt"
    with open(file, 'w') as file:
        file.write("Youknowwho\n")
print("text files are created")

#7th
def copy(fr, to):
    with open(fr, 'r') as fr, open(to, 'w') as to:
        to.write(fr.read())
A = "test doc.txt"
B = "test doc3.txt"
copy(A, B)

#8th

def delete(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File has been deleted.")
        else:
            print("Permission denied.")
    else:
        print("File does not exist.")

path = "test doc3.txt"
delete(path)

#9th
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w", encoding="utf-8") as file:
        file.write(f"Файл {letter}.txt создан успешно.")