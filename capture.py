import cv2
import numpy as np

cap = cv2.VideoCapture(0)  
ret, frame = cap.read()
cv2.imwrite('MyPic.jpg', frame)
