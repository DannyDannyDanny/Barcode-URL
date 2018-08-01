# %% init
import json
import barcode

barcodes = {'OP0001':'https://google.com'}
barcodes['OP0002'] = 'https://dannydannydanny.github.io'
path_json = './python/data/barcodes.json' # Dev

# %% Write dictionary to json file
with open(path_json, 'w') as f:
    json.dump(barcodes, f)

# %% Read dictionary from json file
with open(path_json,'r') as f:
    barcodes = json.load(f)

# %%
print(2+2)
print(2+2)
print(2+2)
print(2+2)
