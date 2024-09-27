# list contents of a directory
import os

directory_path ="/"

contents = os.listdir(directory_path)

for item in contents:
    print(item)