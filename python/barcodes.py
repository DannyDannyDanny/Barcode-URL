# %% init
import json
import barcode
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

# barcode.PROVIDED_BARCODES[0]

encoder_c128 = barcode.get_barcode_class('code128')

text_to_encode = 'Hello, world!'
filename = 'barcode'

mybarcode = c128(text_to_encode)
fullname = ean.save(path_data+filename)
SVG(filename=path_data+filename+'.svg')
