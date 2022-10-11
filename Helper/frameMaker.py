# image for all frames in a video
import cv2
vidcap = cv2.VideoCapture(r"direcory path for video")
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("directory path and name for file%a.jpg" %
                count, image)  # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
