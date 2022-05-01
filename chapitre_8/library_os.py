import os
import shutil

current_path = os.getcwd()
if not os.path.exists(f"{current_path}/test_files"):
    os.mkdir("test_files")
 
all_objects, _, _ = os.walk(current_path)
files = all_objects[2]

for file_name in files:
    print(file_name)
    if file_name.endswith(".txt") or file_name.endswith(".csv") or file_name.endswith(".json"):
        shutil.move(file_name, f"{current_path}/test_files")
