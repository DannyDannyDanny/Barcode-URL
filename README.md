# Barcode-URL
Software for easily embedding links in to barcodes which can then be decoded by the same software.

## Camera version


## Running pip and pipenv on PC
```
python -m pip install pipenv
python -m pipenv install zbar
```

## Exporting to EXE - only tested on MacOS
`pipenv install`

## Dev Env Setup with Conda
1. Make new conda environment `conda create --name EnvName python=3.6`
2. Start conda environment `source activate EnvName`
3. In environment install ipykernel (as a minimum): `pip install ipykernal <any other packages>`
4. Setup ipykernel `python -m ipykernel install --user --name EnvName`
5. In atom, make **.py** file with `print('Hello, World!')` and shift+enter in text-editor
6. Choose `EnvName` from list of environments

> Note to step 3.
You can also use `conda install --name env-name ipykernel` to install from outside the environment.
