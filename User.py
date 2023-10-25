class User:
    def __init__(self, id, firstname, lastname, username, email, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password

    def get_id(self):
        return self.id
    
    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.lastname
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password

    def __str__(self):
        return f"User: {self.id}, {self.firstname}, {self.lastname}, {self.username}, {self.email}, {self.password}"


class YoungLearner(User):
    def __init__(self, id, firstname, lastname, username, email, password):
        super().__init__(id, firstname, lastname, username, email, password)


class Educator(User):
    def __init__(self, id, firstname, lastname, username, email, password):
        super().__init__(id, firstname, lastname, username, email, password)
    

class Parent(User):
    def __init__(self, id, firstname, lastname, username, email, password):
        super().__init__(id, firstname, lastname, username, email, password)
