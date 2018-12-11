'''
import os 
import cv2 
img_root = './img/'
fps = 24 #保存视频的FPS，可以适当调整 #可以用()或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg *'MJPG'
fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
videoWriter = cv2.VideoWriter('saveVideo.avi',fourcc,fps,(640,480))#最后一个是保存图片的尺寸

for i in range(1,10):
    frame = cv2.imread(img_root+'000'+str(i+1)+'.jpg') 
    print(img_root+'0'+str(i+1)+'.jpg')
    
    print('type(frame)', type(frame)) 
    videoWriter.write(frame) 
for i in range(10,100):
    frame = cv2.imread(img_root+'00'+str(i+1)+'.jpg') 
    print(img_root+'0'+str(i+1)+'.jpg')
    
    print('type(frame)', type(frame)) 
    videoWriter.write(frame) 
for i in range(100,700):
    frame = cv2.imread(img_root+'0'+str(i+1)+'.jpg') 
    print(img_root+'0'+str(i+1)+'.jpg')
    
    print('type(frame)', type(frame)) 
    videoWriter.write(frame)         


videoWriter.release()

'''
import os 
import cv2 
path = './img/'
fps = 24 #保存视频的FPS，可以适当调整 #可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg *'MJPG'
fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
videoWriter = cv2.VideoWriter('./saveVideo.avi',fourcc,fps,(640,480))#最后一个是保存图片的尺寸 
#按顺序循环读取图片
for filename in sorted(os.listdir(path)): 
    print(path+filename)
    frame = cv2.imread(path+filename)
    #print(frame)
    print('type(frame)', type(frame)) 
    
    videoWriter.write(frame) 
videoWriter.release()
'''
import cv2 
import os #图片路径 
im_dir = './img/' 
#输出视频路径 
video_dir = './boy.avi' 
#帧率 
fps = 30 
#图片数 
num = 602 
#图片尺寸 
img_size = (640,480) 
#fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
#opencv2.4 
fourcc = cv2.VideoWriter_fourcc('M','J','P','G') 
#opencv3.0 
videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size) 
#按顺序循环读取图片，图片格式是固定位数
for i in range(1,num): 
    im_name = os.path.join(im_dir, str(i).zfill(4)+'.jpg') 
    frame = cv2.imread(im_name) 
    videoWriter.write(frame) 
    print(im_name)
    print(frame)
    print('type(frame)', type(frame)) 
videoWriter.release() 
print('finish')
'''
