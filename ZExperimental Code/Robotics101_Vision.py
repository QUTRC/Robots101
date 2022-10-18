import cv2
import numpy as np
import time
import picamera
from math import atan,sin,cos,pi,floor
import imutils

# Wherever it says "None" the intention is for you to fill in your own values and names :)


kernel = np.ones((None,None))                       # Define variable for image noise filtering (covered more later)


with picamera.PiCamera() as camera:                 # Start up the picamera using the PiCamera library. For pi4s this may be a bit out of date and the libcamera library is potentially better. For the 3B+ Pis we are using they're great.
    camera.resolution = (640, 480)                  # Currently the only setting I'm changing. With weaker/stronger pis you may have to decrease or increase this. 
                                                    # This performance seems to be nice for a Raspberry Pi 3b+


def cam_setup():
    '''This is a little funtion that initialises the camera object. 
    This is where you change all of your camera settings such as forcing an image width and height in this case. 
    Look at the OpenCV documentation for the VideoCapture functionality if you wish to change more stuff and you can put it in here
    '''
    cap = cv2.VideoCapture(0)                       # Connect to camera 0, this is the camera slot you plugged the camera into
    cap.set(3,320)                                  # set width of the image to 320
    cap.set(4,240)                                  # set the height to 240

    return cap                                      # Return the camera object to use with the rest of the code.

def get_frame(frame):
    '''This function gets passed a frame, and prepares it to be blurred and put into the correct colour space. 
    '''

    frame = cv2.GaussianBlur(frame, (3,3),0)        # Blur frame to decrease sharp edges

    frame = cv2.rotate(frame, None)                 # Use this function if you want to rotate the image a certain way
                                                    # None is the OpenCV code for rotating an image. See their cv2.rotatate documentation.

    hsv_frame = cv2.cvtColor(frame, None)           # Change the colour space using the cvtColor function
                                                    # <Insert OpenCV colour code for converstion>

    return None                                     # Return both the frame and the HSV_frame. You only need the original frame if you intend to draw on it (like bounding boxes, frame rates, etc.)


def find_objects(hsv_frame, frame=None):
    '''Implement the main image processing pipeline for finding objects. Takes the hsv_frame (and optionally the original frame if you wish to draw on it)
    '''

    lower_bound = (None,None,None)                  # The lower and upper bound for your inRange function. This is the pixel data range that you consider to be indicative of an object.
    upper_bound = (None,None,None)                  # (h,s,v)
                                                    # (h,s,v)
                                                    
    binary_image = cv2.inRange(None,None,None)      # Create a "binary image" using your colour space ranges. Anything inside the range specified will be assigned a 1 and anything outside will be a 0 in terms of the image data.
                                                    # Look at the inRange documentation for openCV for instructions on how to use this image
                                                    # To display your result so far, comment everything below this point and use the "imshow" function. Usage of this function can be found in the OpenCV documentation.
                                                    
    filtered = cv2.morphologyEx(None, None, None)   # Now filter out all the noise in your image using the kernel specified at the top of your code. You will want to dilate and close the model. 
                                                    # There is a morphologyEx operation that does both of these things. Experiment with different kernel sizes and morphology operations to see how your image gets filtered
                                                    # To display your result so far, comment everything below this point and use the "imshow" function. Usage of this function can be found in the OpenCV documentation.
                                                    
                                                    # At this point you will have a nice 'mask' showing your object. Feel free to take things further using the contours function and starting to research methods of doing distance and angle measurements to your identified objects!
                                                    
    return None, None                               # Return the information you want to return (This could be the filtered image, the binary image, the distance to objects or angle to objects. Whatever your program needs at the current time.)



# This if statement protects your main loop and will not execute it if you call this file as a library. When you run a file, it is given the name "__main__" but when it is imported as a library
# it is not. This means this file is set up to be safely called as a library.
if __name__ == "__main__":
    
    cap = cam_setup()                               # Initialise the camera object to start a new video feed outside the loop

    while True:                                     # This would normally be a really bad idea but we have 2 break statements in this loop that allow it to exit.

        key = cv2.waitKey(None)                     # This function gives you the ability to add a small delay (in miliseconds) and it will try to detect you pressing a keyboard key. (e.g. an 'a' or a 'h')
        ret, frame = cap.read()                     # ret is a boolean that returns True when an image was successfully returned and False when it failed to read an image.
        if not ret:
            break
            
        start = time.time()                                         # Using the time library to calculate framerate and show performance
        None = get_frame(frame)                                     # Return the frame
        None, None = find_objects(hsv_frame, frame)                 # Use the frame to find objects
        None = 1/(time.time() - start)                              # Just framerate things
        cv2.putText(frame, 'Framerate: %05.3f' %(Framerate) ,       # Draw the framerate on the original image
        (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)   

        # cv2.imshow('Orig_img',frame)              # Using imshow to show stuff
        # cv2.imshow('hsv_img' ,hsv_frame)
        # cv2.imshow('binary', binary_image)
        # cv2.imshow('filtered', filtered)


        if cv2.waitKey(5) == ord('q'):
            break
    
    cv2.destroyAllWindows()                         # Destroy the windows at the end of your code for cleanup.
    cap.release()                                   # Release the camera object.
    
    https://automaticaddison.com/how-to-set-up-real-time-video-using-opencv-on-raspberry-pi-4/
        
        
        
#         ---------------------------- Experimental Vision code courtesy of: https://blog.paralect.com/post/object-detection-image-and-video
## 1. Create "Set Mask" window with default HSV range to detect blue color
SET_MASK_WINDOW = "Set Mask"
cv.namedWindow(SET_MASK_WINDOW, cv.WINDOW_NORMAL)
cv.createTrackbar("Min Hue", SET_MASK_WINDOW, 90, 179, noop)
cv.createTrackbar("Max Hue", SET_MASK_WINDOW, 140, 179, noop)
cv.createTrackbar("Min Sat", SET_MASK_WINDOW, 74, 255, noop)
cv.createTrackbar("Max Sat", SET_MASK_WINDOW, 255, 255, noop)
cv.createTrackbar("Min Val", SET_MASK_WINDOW, 0, 255, noop)
cv.createTrackbar("Max Val", SET_MASK_WINDOW, 255, 255, noop)

## 2. Capture from default camera
videoCapture = cv.VideoCapture(0)

while True:
    ## 3. Capture video from camera and convert to HSV color space
    _, capturedVideo = videoCapture.read() # video
    # rotate video 180 degrees (it starts upside down on Windows)
    # capturedVideo = cv.flip(capturedVideo, 1) # Win                                
    capturedVideo = cv.resize(capturedVideo, None, None, fx=0.5, fy=0.5) # macOS
    capturedVideoHsv = cv.cvtColor(capturedVideo, cv.COLOR_BGR2HSV)

    ## 4. Get min and max HSV values from Set Mask window
    minHue = cv.getTrackbarPos("Min Hue", SET_MASK_WINDOW)
    maxHue = cv.getTrackbarPos("Max Hue", SET_MASK_WINDOW)
    minSat = cv.getTrackbarPos("Min Sat", SET_MASK_WINDOW)
    maxSat = cv.getTrackbarPos("Max Sat", SET_MASK_WINDOW)
    minVal = cv.getTrackbarPos("Min Val", SET_MASK_WINDOW)
    maxVal = cv.getTrackbarPos("Max Val", SET_MASK_WINDOW)
    minHsv = np.array([minHue, minSat, minVal])
    maxHsv = np.array([maxHue, maxSat, maxVal])

    ## 5. Create mask and result (masked) video
    # params: input array, lower boundary array, upper boundary array
    mask = cv.inRange(capturedVideoHsv, minHsv, maxHsv)
    # params: src1	array, src2 array, mask
    resultVideo = cv.bitwise_and(capturedVideo, capturedVideo, mask=mask)

    ## 6. Show videos
    cv.imshow("Captured Video", capturedVideo)
    # cv.imshow("Mask", mask)  # optional
    cv.imshow("Result (Masked) Video", resultVideo)
    if cv.waitKey(1) == 27: break   # Wait Esc key to end program

