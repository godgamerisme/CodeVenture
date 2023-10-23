from User import *

#TODO: User Authenticate Class needs to take in module array as well to create a data when registering a new user
class UserAuthenticate:
    def __init__(self, db, data_obj, users_array):
        """
        :param db: ModuleDatabase object
        :param data_obj: data read from json
        :param users_array: array of User objects
        """
        self.db = db
        self.data = data_obj
        self.users = users_array


    def validate_name(self, name):
        if len(name) <= 10 and name.isalpha():
            return True
        return False

    def validate_password(self, password):
        if 5 <= len(password) <= 15:
            return True
        return False

    def validate_usertype(self, usertype):
        if usertype.lower() in ["younglearner", "educator", "parent"]:
            return True
        return False
        

    def validate_email(self, email):
        # Make sure email is not empty and unique
        if email != "" and "@" in email and email.endswith(".com") and email not in [user.email for user in self.users]:
            return True
        return False

    def register(self, new_firstname, new_lastname, new_password, email, new_usertype):
        if self.validate_name(new_firstname) and self.validate_name(new_lastname) and self.validate_password(new_password) and self.validate_email(email) and self.validate_usertype(new_usertype):
            # Auto generate user ID
            id = len(self.data) + 1

            #Process the input
            new_firstname = new_firstname[0].upper() + new_firstname[1:].lower()

            new_lastname = new_lastname[0].upper() + new_lastname[1:].lower()

            # Create user username based on the name and ID
            username = new_firstname[:2].lower() + new_lastname[:2].lower() + str(id)

            new_usertype = new_usertype.lower()

            # Create a dictionary for the new object
            pack_data = self.pack_user_data(id, new_firstname, new_lastname, username, email, new_password, new_usertype)

            # Add the new object to json as a new user
            self.data.append(pack_data)
            self.db.write_data(self.data)

            # Create User Object based on usertype
            if new_usertype == "younglearner":
                new_user = YoungLearner(id, new_firstname, new_lastname, username, email, new_password)
            elif new_usertype == "educator":
                new_user = Educator(id, new_firstname, new_lastname, username, email, new_password)
            elif new_usertype == "parent":
                new_user = Parent(id, new_firstname, new_lastname, username, email, new_password)
            self.users.append(new_user)

            print("Register successfully\n")
            print(f"Your username is {username}\n")
            print(f"Your password is {new_password}\n")
            return True
        else:
            print("Register failed\n")
            return False

    def pack_user_data(self, id, firstname, lastname, username, email, password, usertype):
        return {
            "id": id,
            "firstname": firstname,
            "lastname": lastname,
            "username": username,
            "email": email,
            "password": password,
            "usertype": usertype
        }

    def login(self, username, password):

        # Check if username exists
        user = next((user for user in self.users if user.username == username), None)
        if user:
            # Check if password is correct
            if user.password == password:
                print("Login successful\n")
                return user
            else:
                print("Login failed\n")
                return False
        else:
            print("Login failed\n")
            return False

    def reset_password(self, email, new_password):
        # Check if email exists
        user = next((user for user in self.users if user.email == email), None)
        if user:
            # Check if password is correct
            if self.validate_password(new_password):
                user.password = new_password

                # Update the data in json
                for user_data in self.data:
                    if user_data["email"] == email:
                        user_data["password"] = new_password
                        self.db.write_data(self.data)
                print("Reset password successfully\n")
                return True

            else:
                print("Invalid password. Password must be 5 to 15 characters long.\n")
                print("Reset password failed\n")
                return False
        else:
            print("Email does not exist\n")
            print("Reset password failed\n")
            return False
