# Rename and Changing File Extension
import os
from PIL import Image

# Reading Folder Path
path = 'directory path'
files = os.listdir(path)
nameFile = 'Image'
index = 0
for index, file in enumerate(files):
    
    # Convert File to RGB Image with JPF format
    # Image.open(os.path.join(path, file)).convert('RGB').save('image%d.jpg' % index)

    # Rename File
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(nameFile),str(index), '.jpg'])))