class UserAuthenticate:
    def __init__(self, db, data):
        self.db = db
        self.data = data

    def validate_name(self, name):
        if len(name) <= 10 and name.isalpha():
            return True
    
    def validate_password(self, password):
        if len(password) >= 5 and len(password) <= 15:
            return True

    def validate_usertype(self, usertype):
        if usertype.lower() in ["younglearner", "educator", "parent"]:
            return True
        
    def register(self, new_firstname, new_lastname, new_password, new_usertype):
        # Auto generate user ID
            id = max(item['id'] for item in self.data) + 1 if self.data else 1

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

            # Create user email based on the name and ID
            new_email = new_firstname[:2].lower() + new_lastname[:2].lower() + f"{id:04}" + "@codeventure.com"

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
            new_object = {
                "id": id,
                "firstname": new_firstname,
                "lastname": new_lastname,
                "username": username,
                "email": new_email,
                "password": new_password,
                "usertype": new_usertype
            }
            # Add the new object to json as a new user
            self.data.append(new_object)
            self.db.write_data(self.data)
            print("New data added successfully\n")
            print("Your email is: " + new_email)

    def login(self, email, password):

        for user in self.data:
            if user["email"] == email and user["password"] == password:
                return user["usertype"]
                

    def reset_password(self):
        pass