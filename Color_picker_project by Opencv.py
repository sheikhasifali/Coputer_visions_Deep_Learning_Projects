#import Libraries

import cv2
import numpy as np 

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("color picker")

def cross(x):
    pass

#create switch
s1= "0:OFF\n1:ON"
cv2.createTrackbar(s1,"color picker",0,1,cross)

#Creating trackbar for adjusting color
cv2.createTrackbar("R","color picker",0,255,cross)
cv2.createTrackbar("G","color picker",0,255,cross)
cv2.createTrackbar("B","color picker",0,255,cross)

while True:
    cv2.imshow("color picker",img)
    if cv2.waitKey(1) & 0xff ==27:
        break
        
    #now get trackbar pos
    s=cv2.getTrackbarPos(s1,"color picker")
    r=cv2.getTrackbarPos("R","color picker") 
    g=cv2.getTrackbarPos("G","color picker")
    b=cv2.getTrackbarPos("B","color picker")
    
    if s==0:
        img[:]=0
    else:
        img[:]=[r,g,b]
cv2.destroyAllWindows()
