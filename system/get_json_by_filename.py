import os
import os.path
file_list = os.listdir("jsons")

for file_name in file_list:
    with open(os.path.join("jsons", file_name), "r") as src_file:
        data = src_file.read()
        print(data)
