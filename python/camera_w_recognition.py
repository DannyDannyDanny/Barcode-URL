import cv2
import pyzbar.pyzbar as pyzbar
from IPython.display import Image
from pyzbar.pyzbar import ZBarSymbol
from matplotlib import pyplot as plt
from time import sleep


print('loading camera stream')
cap = cv2.VideoCapture(0)

print('starting detection - press q to quit')

while(True):
    # Capture frame-by-frame
    #print('reading frame')
    sleep(0.5)
    ret, frame = cap.read()

    barcodes = pyzbar.decode(frame, symbols=[ZBarSymbol.CODE128])

    for barcode in barcodes:
        (x,y,w,h) = barcode.rect

        color = (255,100,100) #BGR 0-255,
        stroke = 3
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontColor = color
        lineType = 2

        cv2.putText(frame, str(barcode.data), (x,y), font, fontScale,fontColor,lineType)
        cv2.rectangle(frame, (x,y),(x+w,y+h),color, stroke)

    ## IF len(barcode) == 1: # lookup in opacc db and go to link

    # Display the resulting frame
    cv2.imshow('feed',cv2.flip(frame,1))
    #cv2.imshow('feed',frame)
    #cv2.imshow('gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print('shutting down')
cap.release()
cv2.destroyAllWindows()
exit()
