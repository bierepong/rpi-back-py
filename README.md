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

## Routes

* GET / client
* GET /status Gets an array of sensor status [0, 0, 0, 0, 0, 0]
* POST /begin {"username": "", "email": "", "balls": 6} Begins a game => {"status": "begin"}
* POST /end End the current game => {"status": "begin", "result": [0, 0, 0, 0, 0, 0]}
