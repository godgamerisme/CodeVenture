import json
from User import *
from typing import List


class UserDatabase:
    def __init__(self, filename):
        """
        Initializes the UserDatabase object
        :param filename: name of the json file
        """
        self.filename = filename
        self.data = self.read_data()
        self.user_array = self.to_user_array()

    def get_user_array(self)->List[User]:
        return self.user_array

    def get_data(self):
        return self.data

    def read_data(self):
        """
        Reads data from json file
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return []

    def write_data(self):
        """
        Writes data to json file
        """
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def to_user_array(self)->List[User]:
        """
        Converts the data from json to an array of User objects
        """
        users = []
        for user in self.data:
            if user["usertype"] == "younglearner":
                users.append(
                    YoungLearner(user["id"], user["firstname"], user["lastname"], user["username"], user["email"],
                                 user["password"], user["usertype"]))
            elif user["usertype"] == "educator":
                users.append(Educator(user["id"], user["firstname"], user["lastname"], user["username"], user["email"],
                                      user["password"], user["usertype"]))
            elif user["usertype"] == "parent":
                users.append(Parent(user["id"], user["firstname"], user["lastname"], user["username"], user["email"],
                                    user["password"], user["usertype"]))
        return users


if __name__ == "__main__":
    db = UserDatabase("./data/users.json")
    data = db.read_data()
    users = db.to_user_array()
    print(users)
    for user in users:
        print(user)
