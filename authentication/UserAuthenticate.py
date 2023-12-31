from User import *
from database.UserDatabase import UserDatabase
from database.ModuleDatabase import ModuleDatabase
from module_manager import ModuleManager
from user_manager import UserManager

#TODO: User Authenticate Class needs to take in module array as well to create a data when registering a new user
class UserAuthenticate:
    def __init__(self):
        """
        :param db: Userdatabase object
        :param data_obj: data read from json
        :param users_array: array of User objects
        """
        self.user_db = UserManager.get_instance().get_user_db()
        self.user_data = self.user_db.get_data()
        self.users = self.user_db.get_user_array()
        self.module_db = ModuleManager.get_instance().get_module_db()
        self.module_data = self.module_db.get_data()
        self.module_array = self.module_db.get_module_array()

    def get_module_array(self):
        """
         get the module array
        :return: array of Module objects
        """
        return self.module_array
    
    def get_module_data(self):
        """
        get the module data
        :return: data read from json
        """
        return self.module_data
    
    def get_module_db(self):
        """
        get the module database
        :return: ModuleDatabase object
        """
        return self.module_db

    def get_users(self):
        """
        get the users array
        :return: array of User objects
        """
        return self.users
    
    def get_user_data(self):
        """
        get the user data
        :return: data read from json
        """
        return self.user_data
    
    def get_user_db(self):
        """
        get the user database
        :return: UserDatabase object
        """
        return self.user_db


    def validate_name(self, name):
        """
        Validate name of user
        :param name: str
        :return: True if name is valid, False otherwise
        """
        if len(name) <= 10 and name.isalpha():
            return True
        return False

    def validate_password(self, password):
        """
        Validate password of user
        :param password: str
        :return: True if password is valid, False otherwise
        """
        if 5 <= len(password) <= 15:
            return True
        return False

    def validate_usertype(self, usertype):
        """
        Validate usertype of user
        :param usertype: str
        :return: True if usertype is valid, False otherwise
        """
        if usertype.lower() in ["younglearner", "educator", "parent"]:
            return True
        return False
        

    def validate_email(self, email):
        """
        Validate email of user
        :param email: str
        :return: True if email is valid, False otherwise
        """
        # Make sure email is not empty and unique
        if email != "" and "@" in email and email.endswith(".com") and email not in [user.email for user in self.users]:
            return True
        return False

    def register(self, new_firstname, new_lastname, new_password, email, new_usertype):
        """
        Register a new user
        :param new_firstname: str
        :param new_lastname: str
        :param new_password: str
        :param email: str
        :param new_usertype: str
        :return: True if register successfully, False otherwise
        """
        if self.validate_name(new_firstname) and self.validate_name(new_lastname) and self.validate_password(new_password) and self.validate_email(email) and self.validate_usertype(new_usertype):
            # Auto generate user ID
            id = len(self.user_data) + 1

            #Process the input
            new_firstname = new_firstname[0].upper() + new_firstname[1:].lower()

            new_lastname = new_lastname[0].upper() + new_lastname[1:].lower()

            # Create user username based on the name and ID
            username = new_firstname[:2].lower() + new_lastname[:2].lower() + str(id)

            new_usertype = new_usertype.lower()

            # Create User Object based on usertype
            if new_usertype == "younglearner":
                new_user = YoungLearner(id, new_firstname, new_lastname, username, email, new_password,new_usertype)
            elif new_usertype == "educator":
                new_user = Educator(id, new_firstname, new_lastname, username, email, new_password,new_usertype)
            elif new_usertype == "parent":
                new_user = Parent(id, new_firstname, new_lastname, username, email, new_password,new_usertype)
            self.users.append(new_user)

            # Create a dictionary for the new object
            pack_data = self.pack_user_data(id, new_firstname, new_lastname, username, email, new_password, new_usertype)

            # Add the new object to json as a new user
            self.user_data.append(pack_data)
            self.user_db.write_data()

            pack_module_progress_data = self.pack_module_progress_data(id,username,len(self.module_array))
            self.module_data["users"].append(pack_module_progress_data)
            self.module_db.write_data()

            # Read all data from json again
            self.user_data = self.user_db.read_data()
            self.users = self.user_db.to_user_array()

            self.module_data = self.module_db.read_data()
            self.module_array = self.module_db.to_module_array()

            print("Register successfully\n")
            print(f"Your username is {username}\n")
            print(f"Your password is {new_password}\n")
            return new_user
        else:
            print("Register failed\n")
            return False

    def pack_user_data(self, id, firstname, lastname, username, email, password, usertype):
        """
        Create a dictionary for the new user object
        """
        obj ={
            "id": id,
            "firstname": firstname,
            "lastname": lastname,
            "username": username,
            "email": email,
            "password": password,
            "usertype": usertype
        }
        if usertype == "parent":
            obj["children"] = []
        return obj
    def pack_module_progress_data(self, user_id,username,num_of_modules):
        """
        Create a dictionary for the new module object
        """
        return {
            "user_id": user_id,
            "username": username,
            "module_progress": [{"module_id": i+1, "completed_tutorials": [], "completed_quiz":[]} for i in range(num_of_modules)]

        }

    def login(self, username, password):
        """
        Login user with username and password
        :param username: str
        :param password: str
        :return: True if login successfully, False otherwise
        """

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
        """
        Reset password of user
        :param email: str
        :param new_password: str
        :return: True if reset successfully, False otherwise
        """
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
