import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("VID20180907095121.mp4")
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    # cv2.namedWindow("capture", 640, 480)
    # cv2.resizeWindow("capture", 648, 480)
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
