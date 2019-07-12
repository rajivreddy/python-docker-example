from pymongo import MongoClient
from pymongo import errors

class DatabaseHelper(object):
    def __init__(self):
        try:
            self.client = MongoClient('127.0.0.1:27017')
            self.db = self.client.production
            self.users = self.db.users
        except errors.ServerSelectionTimeoutError as err:
            print(err)
    def insert_user_to_db(self, user_info):
        return self.users.insert_one(user_info)

    def find_user_and_replace(self,user_info):
        return self.users.find_one_and_replace({"username":user_info['username']},user_info)
    
    def get_user_info_by_name(self, username):
        return self.users.find_one(username)
    def find_user_is_exist(self,username):
        return self.users.count({ 'username': username }, limit = 1)

    

class TestDB(DatabaseHelper):
    def __init__(self):
        try:
            self.client = MongoClient()
            self.db = self.client.test
            self.users = self.db.users
        except errors.ServerSelectionTimeoutError as err:
            print(err)

if __name__ == "__main__":
    database = DatabaseHelper()
