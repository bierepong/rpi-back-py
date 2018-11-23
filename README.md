# Bierepong
## Setup python environment
 * Install python 3.6 (https://github.com/pyenv/pyenv if needed)
 ```
$ pip install --upgrade pip
$ pip install pipenv
```

## Starting bierepong
```
$ git clone https://github.com/bierepong/rpi-back.git
$ cd bierepong
$ pipenv install
```

## Starting API
```
$ python bierepong/api/api.py
```
## Starting serial listener
```
$ python bierepong/serial/listener.py
```

