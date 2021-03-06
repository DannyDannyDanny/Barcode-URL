# %% init
import json
import barcode # barcode.PROVIDED_BARCODES[0]
from IPython.display import SVG

barcodes = {'OP0001':'https://google.com'}
barcodes['OP0002'] = 'https://dannydannydanny.github.io'
path_data = './python/data/' # Dev
file_json = 'barcodes.json'

# %% Write dictionary to json file
with open(path_data+file_json, 'w') as f:
    json.dump(barcodes, f)

# %% Read dictionary from json file
with open(path_data+file_json,'r') as f:
    barcodes = json.load(f)

# %% ENCODING DATA IN A BARDCODE and SHOW BARCODE
encoder_c128 = barcode.get_barcode_class('code128')

text_to_encode = 'Hello, world!'
filename = 'barcode'

mybarcode = encoder_c128(text_to_encode)
fullname = mybarcode.save(path_data+filename)
SVG(filename=path_data+filename+'.svg')


def text_to_barcode_svg(text_to_encode, path, filename):
    encoder_c128 = barcode.get_barcode_class('code128')
    mybarcode = encoder_c128(text_to_encode)
    mybarcode.save(path+filename)
    print('encoded ' + text_to_encode + ' as ' + path + filename)

text_to_barcode_svg('hijim',path_data,'hijim')

text_to_barcode_svg('OP0002',path_data,'OP0002')
text_to_barcode_svg('OP0003',path_data,'OP0003')
text_to_barcode_svg('OP0004',path_data,'OP0004')
