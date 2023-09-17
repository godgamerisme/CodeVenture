class UserAuthenticate:
    def __init__(self, db, data_obj):
        self.db = db
        self.data = data_obj
        

    def validate_name(self, name):
        if len(name) <= 10 and name.isalpha():
            return True
    
    def validate_password(self, password):
        if len(password) >= 5 and len(password) <= 15:
            return True

    def validate_usertype(self, usertype):
        if usertype.lower() in ["younglearner", "educator", "parent"]:
            return True
        
    def register(self, new_firstname, new_lastname, new_password, email, new_usertype):
        if(self.validate_name(new_firstname) and self.validate_name(new_lastname) and self.validate_password(new_password) and self.validate_usertype(new_usertype)):
            # Auto generate user ID
            id = len(self.data) + 1

            # Receiving user firstname
            # while not self.validate_name(new_firstname):
            #     print("First name cannot be longer than 10 characters and should all be alphatbets. Please try again.")
            #     new_firstname = input("Enter First Name: ")
            new_firstname = new_firstname[0].upper() + new_firstname[1:].lower()

            # Receiving user lastname
            # new_lastname = input("Enter Last Name: ")
            # while not self.validate_name(new_lastname):
            #     print("Last name cannot be longer than 10 characters and should all be alphatbets. Please try again.")
            #     new_lastname = input("Enter Last Name: ")
            new_lastname = new_lastname[0].upper() + new_lastname[1:].lower()

            # Create user username based on the name and ID
            username = new_firstname[:2].lower() + new_lastname[:2].lower() + str(id)

            #Validate user password
            # while not self.validate_password(new_password):
            #     print("Password length must be at least 5 and not longer than 15 characters")
            #     new_password = input("Enter Password: ")

            #Validate user usertype
            # while not self.validate_usertype(new_usertype):
            #     print("Please enter a valid usertype (younglearner, educator, parent)")
            #     new_usertype = input("Enter User Type (either one of these: younglearner, educator, parent):")
            new_usertype = new_usertype.lower()

            # Create a dictionary for the new object
            pack_data = self.pack_user_data(id, new_firstname, new_lastname, username, email, new_password, new_usertype)
            # Add the new object to json as a new user
            self.data.append(pack_data)
            self.db.write_data(self.data)
            print("Register successfully\n")
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



    def login(self, email, password):

        for user in self.data:
            if user["email"] == email and user["password"] == password:
                return user["usertype"]
                

    def reset_password(self):
        pass