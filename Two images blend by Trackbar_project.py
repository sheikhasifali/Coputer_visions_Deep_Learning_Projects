#import libraries
import cv2
import numpy as np

img1=cv2.imread("rec.png")
img2=cv2.imread("car.jpeg")
img1=cv2.resize(img1,(600,500))
img2=cv2.resize(img2,(600,500))

def blend():
    pass

#wind open where display images

img=np.zeros((400,400,3),np.uint8)
cv2.namedWindow("win")
#trackbar

cv2.createTrackbar("alpha","win",1,100,blend)
switch=" 0:OFF \n 1:ON"
cv2.createTrackbar(switch,"win",0,1,blend)
while True:
    s=cv2.getTrackbarPos(switch,"win")
    a=cv2.getTrackbarPos("alpha","win")
    n=float(a/100)
    print(n)
    
    if s==0:
        dr=img[:]
    else:
        dr=cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dr,str(a),(20,50),cv2.FONT_ITALIC,2,(0,12,200),2)
    cv2.imshow("image",dr)
    if cv2.waitKey(1) & 0xff ==27: # press escape to closs windows
        break


#cv2.imshow("images",img1)
#cv2.imshow("image",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
