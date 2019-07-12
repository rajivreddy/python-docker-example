import unittest
import sys
import json


from database import TestDB
from app import app

user1 = {
    "username": "rajiv",
    "dataOfBirth":"1991-05-15"
}
user2 = {
    "username": "reddy",
    "dataOfBirth":"1991-05-15"
}
user3 = {
    "username": "rajivreddy",
    "dataOfBirth":"1991-05-15"
}

test_db = TestDB()

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = test_db
        self.db.insert_user_to_db(user1)
        self.db.insert_user_to_db(user3)
    def tearDown(self):
        self.db.users.remove({})

    def test_add_user_responce(self):
        response = self.app.put('user/rajivrdd',data='{"dataOfBirth":"1991-05-15"}',content_type='application/json')
        assert str(response.status_code) == '204'
    def test_invalid_user_responce(self):
        response = self.app.put('user/rajivrdd@',data='{"dataOfBirth":"1991-05-15"}',content_type='application/json')
        assert str(response.status_code) == '400'
    def test_invalid_user_get(self):
        response = self.app.get('user/rajivrdd123')
        # print("invalid user ------"+str(response.status_code))
        assert str(response.status_code) == '404'
    
if __name__ == '__main__':
    unittest.main()
