import cv2
import pyzbar.pyzbar as pyzbar
from IPython.display import Image
from pyzbar.pyzbar import ZBarSymbol
from matplotlib import pyplot as plt


path_data = 'python/data/'
filename = 'barcode'
ext = '.png'

Image(filename=path_data+filename+ext)

# load the input image
img = cv2.imread(path_data+filename+ext,0)
plt.imshow(img)
# find the barcodes in the image and decode each of the barcodes
barcodes = pyzbar.decode(img,symbols=[ZBarSymbol.CODE128])
#decode(Image.open('pyzbar/tests/qrcode.png'), symbols=[ZBarSymbol.CODE128])

for barcode in barcodes:
    print(barcode.data)
    print(barcode.type)
    print(barcode.rect)
    print(barcode.polygon)

    (x,y,w,h) = barcode.rect

    color = (255,100,100) #BGR 0-255,
    stroke = 3
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255,255,255)
    lineType = 2

    cv2.putText(img, str(barcode.data), (x,y), font, fontScale,fontColor,lineType)
    cv2.rectangle(img, (x,y),(x+w,y+h),color, stroke)

plt.imshow(img)


#     for (name,cascade) in cascades.items():
#         regions = cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
#         for (x,y,w,h) in regions:
#             #print(x,y,w,h)
#             color = (255,100,100) #BGR 0-255,
#             stroke = 3
#             font                   = cv2.FONT_HERSHEY_SIMPLEX
#             fontScale              = 1
#             fontColor              = (255,255,255)
#             lineType               = 2
#
#             cv2.putText(frame,name[12:-4], (x,y), font, fontScale,fontColor,lineType)
#             cv2.rectangle(frame,  (x,y),(x+w,y+h),color, stroke)
