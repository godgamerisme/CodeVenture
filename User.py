class User:
    def __init__(self, id, firstname, lastname, username, email):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
    def __str__(self):
        return f"User: {self.id}, {self.firstname}, {self.lastname}, {self.username}, {self.email}"

class YoungLearner(User):
    def __init__(self, id, firstname, lastname, username, email):
        super().__init__(id, firstname, lastname, username, email)
    
class Educator(User):
    def __init__(self, id, firstname, lastname, username, email):
        super().__init__(id, firstname, lastname, username, email)
    

class Parent(User):
    def __init__(self, id, firstname, lastname, username, email):
        super().__init__(id, firstname, lastname, username, email)
    