#import numpy as np
import cv2

#####
#
#
#
#####
#print('loading face cascade')
face_cascade = cv2.CascadeClassifier('./cascades/data/haarcascade_frontalface_alt2.xml')

print('loading camera stream')
cap = cv2.VideoCapture(0)

print('starting loop')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #---> barcode reading every frame

    # Display the resulting frame
    cv2.imshow('feed',cv2.flip(frame,1))
    #cv2.imshow('gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print('shutting down')
cap.release()
cv2.destroyAllWindows()
