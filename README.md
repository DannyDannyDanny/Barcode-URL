# Barcode-URL

>This project is archived

Software for easily embedding links in to barcodes which can then be decoded by the same software - using the devices camera.

Note: Name change to OpAcc (Operator Access) is quite likely to take place soon.

## List of devices 💻
There are three machines:
* **dev** - my dev machine (MacOS)
* **w7** - my work machine
* **w8** - plant floor tablet

## Milestones 🏁
* ~~Write camera session code~~
* ~~Install Anaconda on W7~~
* ~~Move~~ / **Recreate** ~~environment on W7~~
* ~~Test camera stream on W7~~
* Define pilot demo
* Open links see [call OS to open links](https://stackoverflow.com/questions/4216985/call-to-operating-system-to-open-url)
* Generate barcodes
  * ~~Write pre-specified code to generate barcodes~~
  * Write user input code to generate barcodes
  * Output barcodes in `png` format
  * Output barcodes in user friendly format - currently barcodes are output as SVG files. They can manually be converted using `qlmanage -t -s 1000 -o . filename.svg`
* Build Storage
  * Write local barcode reference storage
  * Investigate what data needs to be accessed
  * Investigate how to access this data
* Project management
  * Present OpAcc at IT-project Board?
* ~~Move code to internal repository~~
  * Stop primarily developing on Github repository
  * Get remote access to HT repo
* Complete deployment
  * Test barcode generating code on **w7**
  * Install Anaconda on W8 tablet - **lacking permissions**
  * Install conda environment on **w8** tablet
  * Make the program run **w8** tablet
  * Figure out how to mass deploy to **w8**'s

## Barcodes 📦
This is what a generated barcode might look like :)
![barcode](python/data/barcode.svg)

<<<<<<< HEAD:README_nac.md
## Pilot Demo
A downscoped version of the project needs to be made
### Procedure
* Choose a link
* Open OpAcc
* Enter link
* Add link to DB
* Generate link from DB
* *Print barcode* - how?
* Scan barcode
* Open link


## Environment Management
=======
## Environment Management 🛠
>>>>>>> 60b21de7d7de6203c488d8234b066d50b8691f87:README.md
Official documentation [here](https://conda.io/docs/user-guide/tasks/manage-environments.html)

### Dependencies
* `pip install opencv-python`
* `pip install json`
* `pip install python-barcode` [Read more](https://pypi.org/project/python-barcode/)
* Only for dev: `pip install ipykernal`

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
1. Activate environment `source activate env-name`
2. Export via conda `conda env-name export > environment.yml`

## Conda hacks ✴️
* `conda env list` - List environments
* `conda env-name export > environment.yml` - run from within environment to create template of environment
* `conda env create -f environment.yml` - create environment from template

## ipykernel hacks 🖤
```python
# run terminal commands by using '!'
!cat README.md
```

## Issues 🕷
How do you make a bugs / issues section

#### Importing conda package is a pain
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
