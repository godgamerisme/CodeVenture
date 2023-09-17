from UserDatabase import *

class UserAuthenticate():
    
    def register(data):
        db = UserDatabase("./data/users.json")

        next_id = max(item['id'] for item in data) + 1 if data else 1

        # Take user input for the new object
        # new_id = int(input("Enter ID: "))
        new_firstname = input("Enter First Name: ")
        new_lastname = input("Enter Last Name: ")
        new_username = input("Enter Username: ")
        new_email = input("Enter Email: ")
        new_usertype = input("Enter User Type: ")

        # Create a dictionary for the new object
        new_object = {
            "id": next_id,
            "firstname": new_firstname,
            "lastname": new_lastname,
            "username": new_username,
            "email": new_email,
            "usertype": new_usertype
        }

        for user in data:
            exist = False
            if user["username"] == new_object["username"]:
                exist = True
                print("Data already exists")
                break

        if not exist:
            data.append(new_object)
            db.write_data(data)
            print("New data added successfully")