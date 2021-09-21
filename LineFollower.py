import cv2                                      # importing OpenCV library for Computer Vision operations
import numpy as np                              # importing NumPy library for numerical computations
from gpiozero import LED                        
from serial import Serial                       # importing PySerial module to make use of serial commn.

ser = serial.Serial("/dev/ttyS0",38400)         # creating an object of serial class with baudrate 38400, configured to GPIO RX & TX pin on Raspberry Pi

cap = cv2.VideoCapture(0)                       # object of video capture created, and webcam is accessed
cap.set(3,160)                                  # width of the captured frame is set
cap.set(4,120)                                  # height of the capture frame is set

c=0

while True:                                     # infinite loop to continuosly keep on recieveing frames from webcam
    ret, frame = cap.read()                     # storing recieved frames from webcam and ret, is a boolean cond. checking if frames are recieved are not
    
    low_b = np.array([70,70,70])                # creating an array which represent dark grayish color
    high_b = np.array([0,0,0])                  # creating an array which represent black color
    mask = cv2.inRange(frame, high_b,low_b)     # creating a mask from the frame to identify or pickup colors between low_b and high_b pixel range
    _,contours,hierarchy = cv2.findContours(mask, 1,cv2.CHAIN_APPROX_NONE)  # findContours is used to find contours on the mask image, later to apply it onto the original frame

    if len(contours)>0:                         # entering if at least one contour is detected
        c = max(contours, key=cv2.contourArea)  # finding the largest contour based on max area, which will be used to follow
        M = cv2.moments(c)                      # computing the centre point of the largest contour
        if M["m00"]!=0:
            cx = int(M['m10']/M['m00'])         # computing x coordinate of the centre point
            cy = int(M['m01']/M['m00'])         # computing y coordinate of the centre point
            print("CX:"+str(cx)+" CY:"+str(cy))
            if cx>=320:                         # Tracking the x coordinate of the centre point, if it is greater than 320 pixels, then the centre point of the contour is on the right side, and thus wheelchair has to be turned right
                print("Turn Right")
                ser.write(b'3')                 # Sending serial commands to Arduino to turn right
            if cx<320 and cx>300:               # if x coordinate of centre point it is between 320 & 300 pixels, then the centre point of the contour is at the centre of the frame, and thus wheelchair has to be moved in forward direction
                print("On track")
                ser.write(b'1')                 # Sending serial commands to Arduino to make the motors move forward
            if cx<=300:                         # if x coordinate of centre point it is lesser than 300 pixels, then the centre point of the contour is on the left side, and thus wheelchair has to be turned left
                print("Turn Left")
                ser.write(b'2')                 # Sending serial commands to Arduino to turn left
            cv2.circle(frame,(cx,cy),5,(255,255,255),-1)       # drawing a circle on the original frame as a representation of the centre point, in white color, for convenience
    cv2.drawContours(frame,c,-1,(0,255,0),1)                   # drawing contours detected on the original frame as a representation, in green color, for convenience
    cv2.imshow("Mask",mask)                     # Displaying mask and frame windows
    cv2.imshow("Frame",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):       # To check every second and if q is pressed on the keyboard, the program will stop
        break

cap.release()                                   # Releasing webcam for other use
cv2.destroyAllWindows()                         # Quitting all windows
