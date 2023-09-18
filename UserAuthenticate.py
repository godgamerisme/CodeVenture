from User import *
class UserAuthenticate:
    def __init__(self, db, data_obj,users_array):
        self.db = db
        self.data = data_obj
        self.users = users_array
        

    def validate_name(self, name):
        if len(name) <= 10 and name.isalpha():
            return True
    
    def validate_password(self, password):
        if len(password) >= 5 and len(password) <= 15:
            return True

    def validate_usertype(self, usertype):
        if usertype.lower() in ["younglearner", "educator", "parent"]:
            return True
        
    def validate_email(self, email):
        #make sure email is not empty and unique
        if email != "" and email not in [user.email for user in self.users]:
            return True
        
    def register(self, new_firstname, new_lastname, new_password, email, new_usertype):
        if(self.validate_name(new_firstname) and self.validate_name(new_lastname) and self.validate_password(new_password) and self.validate_email(email) and  self.validate_usertype(new_usertype)):
            # Auto generate user ID
            id = len(self.data) + 1

            # Receiving user firstname
            while not self.validate_name(new_firstname):
                print("First name cannot be longer than 10 characters and should all be alphatbets. Please try again.")
                new_firstname = input("Enter First Name: ")
            new_firstname = new_firstname[0].upper() + new_firstname[1:].lower()

            # Receiving user lastname
            while not self.validate_name(new_lastname):
                print("Last name cannot be longer than 10 characters and should all be alphatbets. Please try again.")
                new_lastname = input("Enter Last Name: ")
            new_lastname = new_lastname[0].upper() + new_lastname[1:].lower()

            # Create user username based on the name and ID
            username = new_firstname[:2].lower() + new_lastname[:2].lower() + str(id)

            #Validate user password
            while not self.validate_password(new_password):
                print("Password length must be at least 5 and not longer than 15 characters")
                new_password = input("Enter Password: ")

            #Validate user usertype
            while not self.validate_usertype(new_usertype):
                print("Please enter a valid usertype (younglearner, educator, parent)")
                new_usertype = input("Enter User Type (either one of these: younglearner, educator, parent):")
            new_usertype = new_usertype.lower()

            # Create a dictionary for the new object
            pack_data = self.pack_user_data(id, new_firstname, new_lastname, username, email, new_password, new_usertype)
            # Add the new object to json as a new user
            self.data.append(pack_data)
            self.db.write_data(self.data)

            #create User Object based on usertype
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
        else:
            print("Register failed\n")

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
                print("Login successfully\n")
                return user
            else:
                print("Login failed\n")
        else:
            print("Login failed\n")
                

    def reset_password(self,email,new_password):
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

            else:
                print("Password length must be at least 5 and not longer than 15 characters\n")
                print("Reset password failed\n")
        else:
            print("Email does not exist\n")
            print("Reset password failed\n")
