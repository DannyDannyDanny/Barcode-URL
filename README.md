# Barcode-URL
Software for easily embedding links in to barcodes which can then be decoded by the same software.

## Camera version

## Environment Management
Official documentation [here](https://conda.io/docs/user-guide/tasks/manage-environments.html)

### Dev Env Setup with Conda
1. Make new conda environment `conda create --name env-name python=3.6`
2. Start conda environment `source activate env-name`
3. In environment install ipykernel (as a minimum): `pip install ipykernal <any other packages>`
4. Setup ipykernel `python -m ipykernel install --user --name env-name`
5. In atom, make **.py** file with `print('Hello, World!')` and shift+enter in text-editor
6. Choose `env-name` from list of environments

> Note to step 3.
You can also use `conda install --name env-name ipykernel` to install from outside the environment.

### Env export via conda
1. Activaet environment `source activate env-name`
2. Export via conda `conda env-name export > environment.yml`
