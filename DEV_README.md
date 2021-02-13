# EasyROI

## Developer Manual

### Requirements

```
python3
cv2
numpy
```


## Running test code

* Create virtual environment and activate it

```sh
python3 -m venv venv_easy_roi
source venv_easy_roi/bin/activate
```

* install requirements.txt

```sh
pip3 install -r requirements.txt
```

```sh
git clone https://github.com/saharshleo/easyROI.git
```

```sh
python dev_main.py
```


## Packaging

* Create `setup.py`
* Create `README.md`
* Folder structure should be

    easyROI 
    .  
    ├── EasyROI  
    │   ├── __init__.py  
    │   ├── utils.py  
    │   └── easyROI.py  
    ├── setup.py  
    ├── LICENSE  
    └── README.md  

* Create packaging environment
  
```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install wheel
pip3 install twine
```

* Creating wheel file

```sh
python setup.py sdist bdist_wheel
```

* Publishing

```sh
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

* For testing published library
* Create testing environment

```sh
python3 -m venv venv_test
source venv_test/bin/activate
```

* Install or Upgrade `EasyROI`

```sh
pip3 install EasyROI

OR

pip3 install EasyROI --upgrade
```

* Test library

```sh
python test_library.py
```


## TODO

See progress in [TODO.md](TODO.md)