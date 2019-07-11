# Python Docker Example 

## Requirements
* Docker
* docker-compose

### Usage:
1. Clone the repo 
2. Build docker images 

```
$ git clone git@github.com:rajivreddy/python-docker-example.git
$ cd python-docker-example
$ docker-compose build
```
3. Ruuning Container
```
$ docker-compose up -d
```
```
$ python-docker-example git:(master) ✗ docker-compose ps
     Name                  Command             State            Ports
------------------------------------------------------------------------------
revolt_mongo_1   docker-entrypoint.sh mongod   Up      0.0.0.0:27017->27017/tcp
revolt_web_1     python ./example.py           Up      0.0.0.0:5000->5000/tcp
➜  python-docker-example git:(master) ✗
```
You can access APIs on http://127.0.0.1:5000/user/<username>