#os module
import os
directory_path = "/Users/srika"
contents = os.listdir(directory_path)

for item in contents:
    print(item)