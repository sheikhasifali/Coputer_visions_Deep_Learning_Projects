import cv2
import numpy as np

img=cv2.imread("ball.jpg")
img=cv2.resize(img,(400,300))

cv2.namedWindow("Color Image")

def null(x):
    pass
cv2.createTrackbar("lower_h","Color Image",0,255,null)
cv2.createTrackbar("lower_s","Color Image",0,255,null)
cv2.createTrackbar("lower_v","Color Image",0,255,null)

cv2.createTrackbar("Upper_h","Color Image",255,255,null)
cv2.createTrackbar("Upper_s","Color Image",255,255,null)
cv2.createTrackbar("Upper_v","Color Image",255,255,null)

while True:
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    l_h=cv2.getTrackbarPos("lower_h","Color Image")
    l_s=cv2.getTrackbarPos("lower_s","Color Image")
    l_v=cv2.getTrackbarPos("lower_v","Color Image")
    
    u_h=cv2.getTrackbarPos("Upper_h","Color Image")
    u_s=cv2.getTrackbarPos("Upper_s","Color Image")
    u_v=cv2.getTrackbarPos("Upper_v","Color Image")
    
    lower=np.array([l_h,l_s,l_v])
    upper=np.array([u_h,u_s,u_v])
    
    mask=cv2.inRange(hsv,lower,upper)
    
    result=cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow("orignal",img)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    
    if cv2.waitKey(1) & 0xff==27:
        break
cv2.destroyAllWindows()
