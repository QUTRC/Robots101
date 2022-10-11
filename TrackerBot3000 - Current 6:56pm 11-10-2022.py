# ---------------------------------------------------------------- Experimental Code: Lines 1 to 27, - DISPLAY LIVE FEED
# Code to display picam as a video stream, does not save, is a raw feed. - Source code started: 4th Sept 2022 created by TheWarlock27
import cv2
import numpy as np
import time
import picamera #Picam info: The sensor itself has a native resolution of 5 megapixel, and has a fixed focus lens onboard. In terms of still images, the camera is capable of 2592 x 1944 pixel static images, and also supports 1080p @ 30fps, 720p @ 60fps and 640x480p 60/90 video recording.
from math import atan,sin,cos,pi,floor
import imutils
from picamera import PiCamera
from picamera.array import PiRGBArray

#Motor Setups
from mobility import *
import time
if __name__ == "__main__":

#--------------------------------------------------- OG Code - Thewarlock27 and Dingo
#camera = PiCamera()
cap = cv2.VideoCapture(0)
with picamera.PiCamera() as camera:                 # Start up the picamera using the PiCamera library. For pi4s this may be a bit out of date and the libcamera library is potentially better. For the 3B+ Pis we are using they're great.
    camera.resolution = (640, 480)
#time.sleep(2)

if (cap.isOpened()== False):  #Check if camera opened successfully
  print("Error opening video stream or file")

while(cap.isOpened()):   #Read until video is completed
  ret, frame = cap.read()   #Capture frame-by-frame
  if ret == True:
    cv2.imshow('Stream',frame)      # Display the resulting frame
    print ("streaming")
    
#     Our operations on the frame come here - line 16 should convert feed to greyscale.
#     gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     # Our operations on the frame come here

# 
#     Display the resulting frame
#     cv2.imshow('RGB',gray_scale)
#     #cv2.imshow('Orig_img',frame)             
#     #cv2.imshow('hsv_img' ,hsv_frame)
#     #cv2.imshow('binary', binary_image)
#     #cv2.imshow('filtered', filtered)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):      # Press lowercase Q on keyboard to exit
        break
  
  else: 
    print("No Feed")
    break     #Break the loop


cap.release()  # When everything done, release the video capture object
cv2.destroyAllWindows()  # Closes all the frames

#--------------------------------------------

    # Initialise motors
    MotorA = Motor(17,18)
    MotorB = Motor(22,23)

    # Each motor can be controlled individually like so:
    MotorA.forward(100)
    time.sleep(1)
    MotorA.stop()
    time.sleep(1)
    MotorA.backward(100)
    time.sleep(1)
    MotorA.stop()

    # Or you can control both motors at the same time using the static methods:
    Motor.moveForward(100)
    time.sleep(1)
    Motor.moveReverse(100)
    time.sleep(1)
    Motor.stopAll()
    Motor.rotate(100)
    time.sleep(1)
    Motor.rotate(-100)
    time.sleep(1)
    Motor.stopAll()
    

    # The library also does the cleanup at the end of execution. So even while running, if the program ends
    # Motors *Should* stop automatically.
    # However, if you want to nicely clean up after yourself, the Motor.cleanup() method will make sure everything is nice and tidy when you're done

    Motor.cleanup()

