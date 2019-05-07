#-*- coding:utf-8 -*
import cv2

vid = cv2.VideoCapture('2person_camera.mp4') #读入视频文件

c=0

rval=vid.isOpened()

#timeF = 1  #视频帧计数间隔频率

while rval:   #循环读取视频帧

    c = c + 1
    
    ret, frame = vid.read()
    #if(c%timeF == 0): #每隔timeF帧进行存储操作

#        cv2.imwrite('smallVideo/smallVideo'+str(c) + '.jpg', frame) #存储为图像

    if ret:

        cv2.imwrite('./frame/2person_camera/'+str(c).zfill(8) + '.jpg', frame) # zfill()方法返回指定长度的字符串，原字符串右对齐，前面填充0

        cv2.waitKey(1)

    else:

        break

vid.release()
