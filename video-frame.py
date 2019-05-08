#-*- coding:utf-8 -*
'''
#保存每一帧视频
import cv2
vid = cv2.VideoCapture('test.avi') #读入视频文件
c=0
rval=vid.isOpened()
while rval:   #循环读取视频帧

    c = c + 1
    rval, frame = vid.read()
    if rval:
        cv2.imwrite('./frame/2person_camera/'+str(c).zfill(8) + '.jpg', frame) # zfill()方法返回指定长度的字符串，原字符串右对齐，前面填充0
        cv2.waitKey(1)
    else:
        break
vid.release()

'''



#视频帧计数间隔保存
import cv2
vc = cv2.VideoCapture('./test.avi') #读取视频文件
c = 0
if vc.isOpened():#判断是否正常打开
    rval,frame = vc.read()
else:
    rval = False
 
timeF = 22 #视频帧计数间隔频率
 
while rval: #循环读取视频帧
    rval, frame = vc.read()
    if (c%timeF == 0): #每隔timeF帧进行存储操作
        cv2.imwrite('./JPEGImages/'+str(c)+'.jpg',frame) # 存储为图像

    c = c + 1
    cv2.waitKey(1)
vc.release()







