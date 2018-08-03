import cv2
import pyzbar.pyzbar as pyzbar
from IPython.display import Image

path_data = 'python/data/'
filename = 'barcode'
ext = '.png'

Image(filename=path_data+filename+ext)

# load the input image
img = cv2.imread(path_data+filename+ext,0)

# find the barcodes in the image and decode each of the barcodes
barcodes = pyzbar.decode(img)

barcodes
