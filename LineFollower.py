import cv2
import numpy as np
from gpiozero import LED

motor1 = LED(8)
motor2 = LED(7)

cap = cv2.VideoCapture(0)
cap.set(3,160)
cap.set(4,120)

c=0

while True:
    ret, frame = cap.read()
    #imghsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    low_b = np.array([70,70,70])
    high_b = np.array([0,0,0])
    mask = cv2.inRange(frame, high_b,low_b)
    _,contours,hierarchy = cv2.findContours(mask, 1,cv2.CHAIN_APPROX_NONE)

    if len(contours)>0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"]!=0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print("CX:"+str(cx)+" CY:"+str(cy))
            if cx>=320:
                print("Turn Right")
                motor1.off()
                motor2.on()
            if cx<320 and cx>300:
                print("On track")
                motor1.on()
                motor2.on()
            if cx<=300:
                print("Turn Left")
                motor1.on()
                motor2.off()
            cv2.circle(frame,(cx,cy),5,(255,255,255),-1)
    cv2.drawContours(frame,c,-1,(0,255,0),1)
    cv2.imshow("Mask",mask)
    cv2.imshow("Frame",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
