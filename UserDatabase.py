import json
from User import *

class UserDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_data()

    def read_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return []

    def write_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def to_user_array(self):
        users = []
        for user in self.data:
            if user["usertype"] == "younglearner":
                users.append(YoungLearner(user["id"], user["firstname"], user["lastname"], user["username"], user["email"], user["password"]))
            elif user["usertype"] == "educator":
                users.append(Educator(user["id"], user["firstname"], user["lastname"], user["username"], user["email"], user["password"]))
            elif user["usertype"] == "parent":
                users.append(Parent(user["id"], user["firstname"], user["lastname"], user["username"], user["email"], user["password"]))
        return users

if __name__ == "__main__":
    db = UserDatabase("./data/users.json")
    data = db.read_data()
    users = db.to_user_array()
    print(users)
    for user in users:
        print(user)