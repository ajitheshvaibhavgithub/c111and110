import os
import shutil

path="c:/users/hp/downloads"
listoffile=os.listdir(path)
for file in listoffile:
    name,ext=os.path.splitext(file)
    print(name)
    print(ext) 