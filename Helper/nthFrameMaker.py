# images for every nth frame in a video
import os
import cv2
pathOut = r"directory path for frames"
count = 0
counter = 1
vid = r"direcory path for video"
cap = cv2.VideoCapture(vid)
count = 0
counter += 1
success = True
while success:
    success, image = cap.read()
    print('read a new frame:', success)
    # make images file every nth frame
    if count % 15 == 0:
        cv2.imwrite(pathOut + 'frame%d.jpg' % count, image)
    count += 1
