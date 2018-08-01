# Barcode-URL
Software for easily embedding links in to barcodes which can then be decoded by the same software - using the devices camera.

Note: Name change to OpAcc (Operator Access) is quite likely to take place soon.

## Milestones
* ~~Install Anaconda on W7 laptop~~
* Move environment to W7 laptop - **some issue**
* Install Anaconda on W8 tablet - **lacking permissions**
* Install conda environment on W8 tablet
* Make the program run W8 tablet

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

## Conda hacks
* `conda env list` - List environments
* `conda env-name export > environment.yml` - run from within environment to create template of environment
* `conda env create -f environment.yml` - create environment from template


### Issue importing following
```
ResolvePackageNotFound:
- ncurses==6.1=h0a44026_0
- libcxx==4.0.1=h579ed51_0
- zlib==1.2.11=hf3cbc9b_2
- libedit==3.1.20170329=hb402a30_2
- tbb==4.3_20141023=0
- numpy-base==1.14.5=py35ha9ae307_0
- mkl_random==1.0.1=py35h78cc56f_0
- numpy==1.14.5=py35h9bb19eb_0
- tk==8.6.7=h35a86e2_3
- libffi==3.2.1=h475c297_4
- readline==7.0=hc1231fa_4
- hdf5==1.8.20=hfa1e0ec_1
- mkl_fft==1.0.4=py35h5d10147_0
- openssl==1.0.2o=h26aff7b_0
- xz==5.2.4=h1de35cc_4
- libgfortran==3.0.1=h93005f0_2
- sqlite==3.24.0=ha441bb4_0
- python==3.5.5=h0a44026_3
- libcxxabi==4.0.1=hebd6815_0
```
