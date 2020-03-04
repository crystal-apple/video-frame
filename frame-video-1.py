import os 
import cv2
path = './img/'
fps = 24
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter('./saveVideo.avi',fourcc,fps,(960,544))
for filename in sorted(os.listdir(path)):
    print(path+filename)
    frame = cv2.imread(path+filename)
    print('type(frame)',type(frame))
    videoWriter.write(frame)
videoWriter.release()
