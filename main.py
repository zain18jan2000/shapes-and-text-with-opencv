import cv2
import numpy as np

img = np.zeros((500,700,3), dtype= np.uint8)

#cv2.line(img,(200,200),(500,200),(255,255,255),2)

#cv2.rectangle(img,(150,150),(400,400),(255,255,255),1)

#cv2.circle(img,(250,250),100,(255,0,0),-1)

cv2.putText(img,'ZAIN',(200,200),cv2.FONT_HERSHEY_TRIPLEX,2,(0,255,0),2)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()