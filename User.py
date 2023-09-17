class User:
    def __init__(self, id, firstname, lastname, username, email, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
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
    