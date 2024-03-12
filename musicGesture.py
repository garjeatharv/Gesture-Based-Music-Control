import time
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import pyautogui as py

width, height = int(1280),int(720)

#cam setup
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

#variables
imgNumber = 3
hs,ws = int(120*1),int(213*1)
gestureThreshold = 300 
buttonPressed = False
buttonCounter = 0
buttonDelay = 30

detector = HandDetector(detectionCon=0.8,maxHands=1)

#get list of presntaion images
# pathImage = sorted(os.listdir(folderPath), key=len)
while True:

    #import Images
    success, img = cap.read()
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img)
    # cv2.line(img,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),10)
    if hands and buttonPressed is False:
        hand = hands[0]
        fingures = detector.fingersUp(hand)
        cx,cy = hand['center']

        #gesture 1- right
        if fingures == [0,0,0,0,1]:
            print("Right")
            py.press('right')
            time.sleep(1)
            
        
        #gesture 2- left
        if fingures == [1,0,0,0,0]:
            print("left")
            py.press('left')
            time.sleep(1)

        #gesture 3- up
        if fingures == [0,1,0,0,0]:
            print("up")
            py.press('volumeup')
            time.sleep(1)
            time.sleep(1)

        #gesture 4- down
        if fingures == [0,1,1,0,0]:
            print("down")
            py.press('volumedown')
            time.sleep(1)

        #gesture 5 - pause/play
        if fingures == [1,1,1,1,1]:
            print("space")
            # py.press('space')
            py.press('playpause')
            time.sleep(1)
        
        #gesture 6- next song
        if fingures == [0,0,0,1,1]:
            print("Next Song")
            py.keyDown('shiftleft')
            py.press('n')
            py.keyUp('shiftleft')
            time.sleep(1)
        
        #gesture 7- previos song
        if fingures == [0,0,1,1,0]:
            print("Previous Song")
            py.keyDown('shiftleft')
            py.press('p')
            py.keyUp('shiftleft')
            time.sleep(1)

        #gesture 8 - mute
        if fingures == [0,1,1,1,0]:
            print("Mute")
            py.press('volumemute')
            time.sleep(1)

    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break