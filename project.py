import os
import shutil
from_dir="C:/Users/samsung/Downloads"
to_dir="C:/Users/samsung/Desktop/downloded_files"
list_of_files=os.listdir(from_dir)
#print(list_of_files)
for file in list_of_files:
    root,ext=os.path.splitext(file)
   # print(root)
   # print(ext)
    if ext=="":
        continue
    if ext in [".txt", ".doc", ".docx", ".pdf"]:
        path1=from_dir+"/"+file
        path2=to_dir+"/"+"document_files"
        path3=to_dir+"/"+"document_files"+"/"+file
        print("path1 : ",path1)
        print("path3 : ",path3)
        if os.path.exists(path2):
            print("moving...",file)
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("moving...",file)
            shutil.move(path1,path3)
