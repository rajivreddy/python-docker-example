from flask import Flask, jsonify, request
from functools import wraps
from datetime import datetime
from pymongo import MongoClient
import json
import os


client = MongoClient(os.getenv('DB_URL'))
db = client.ContactDB

app = Flask(__name__)

def validate_username(f):
    @wraps(f)
    def wrapper(username):
        print('Calling decorated function')
        print(username)
        if username.isalnum():
            return f(username)
        else:
            msg = "Incorrect Username format, should be alpha numeric"
            return jsonify({"error": msg}), 400
    return wrapper

def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper


def validate_dob(f):
    @wraps(f)
    def wrapper(*args, **kw):
        print(request.json["dataOfBirth"])
        try:
            # Validating the DOB format and Todays date is greater than Given date
            if (datetime.strptime(request.json["dataOfBirth"],'%Y-%m-%d') ) and (datetime.today() > datetime.strptime(request.json["dataOfBirth"],"%Y-%m-%d")):
                # Validating if diff between todays and given date is not equal to zero 
                if (datetime.today()-datetime.strptime(request.json["dataOfBirth"],"%Y-%m-%d")).days !=0:
                    pass
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            msg = "Incorrect data format, should be YYYY-MM-DD"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper


@app.route("/")
def helloworld():
    return jsonify({'result':"Helloworld"}),200

@app.route("/user/<username>",methods=['PUT'])
@validate_username
@validate_json
@validate_dob
def updateusersdb(username):
    try:
        if db.Users.count({ 'username': username }, limit = 1) == 0:
            status = db.Users.insert_one({
                        "username":username,
                        "dataOfBirth":request.json["dataOfBirth"]
                    })
            print(status)
            return jsonify({}),204
        else:
            status = db.Users.find_one_and_replace({
                        "username":username},
                        {"username":username,
                        "dataOfBirth":request.json["dataOfBirth"]
                    })
            print(status)
            return jsonify({}),204
    except:
        return jsonify({}),404
    

@app.route("/user/<username>",methods=['GET'])
@validate_username
def getusersdob(username):
    print(username)
    if db.Users.count({ 'username': username }, limit = 1) != 0:
        print("hurry")
        dob=db.Users.find_one({ 'username': username})
        print(dob["dataOfBirth"].__class__)
        numbe_of_days = abs(datetime.today().timetuple().tm_yday-datetime.strptime(dob["dataOfBirth"],"%Y-%m-%d").timetuple().tm_yday)
        if numbe_of_days == 0:
            return jsonify({"message":"Hello, "+username+"! Happy Birthday!"}),200
        else:
            return jsonify({"message":"Hello, "+username+"! Your Birthday is in "+ str(abs(365-numbe_of_days))+ "day(s)"}),200
    else:
        return  jsonify({"message":"User Not Found"}),404



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)