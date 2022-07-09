import cv2 
import time 
import  numpy as np 
import HandTrackingMOdel as htm 
import math 

cap = cv2.VideoCapture(0)
detector = htm.handTracker()

tipsid = [4,8,12,16,20]


while 1:
    seccess , img = cap.read()
    img = detector.handsFinder(img)
    lmlist = detector.positionFinder(img , draw=False)
    if len(lmlist) != 0 :
        fingers = []
        
        # for the thump
        if lmlist[tipsid[0]][1] > lmlist[tipsid[0]- 1 ][1] :
            fingers.append(1)
        else : 
             fingers.append(0)
        
        
        # for 4 fingers 
        for i_d in range(1,5) :
            if lmlist[tipsid[i_d]][2] < lmlist[tipsid[i_d]- 2 ][2] : 
                fingers.append(1)
            else :
                fingers.append(0)
        
        total = fingers.count(1)
        cv2.putText(img, str(total), (80,375), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255) , 5)
        
    
    cv2.imshow('image' , img)
    cv2.waitKey(1)
    