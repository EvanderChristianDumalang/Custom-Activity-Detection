# Change file extension
import os

dir =(r"directory path")
for i in os.listdir(dir):
    files = os.path.join(dir,i)
    split= os.path.splitext(files)
    if split[1]=='.txt':
       os.rename(files,split[0]+'.csv')