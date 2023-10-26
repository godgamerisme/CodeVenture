from typing import List
from Modules import *

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
        self.progress= []
        self.all_tutorials_completed = []
        self.all_quizzes_completed = []

    def get_progress(self):
        return self.progress
    
    def get_all_tutorials_completed(self):
        return self.all_tutorials_completed
    
    def get_all_quizzes_completed(self):
        return self.all_quizzes_completed
    
    def populate_user_progress(self, module_array:List[Module]):
        """
        Search through the module array and add the user's progress to the user object
        """
        #Reset the progress list,all tutorials completed and all quizzes completed
        self.progress = []
        self.all_tutorials_completed = []
        self.all_quizzes_completed = []

        for module in module_array:
            for progress in module.get_user_progress():
                if progress.get_user_id() == self.id:
                    #Check if the progress is already in the user's progress list
                    if progress not in self.progress:
                        self.progress.append(progress)
                        break
        #populate all tutorials completed and all quizzes completed
        for progress in self.progress:
            self.all_tutorials_completed.extend(progress.get_completed_tutorials())
            self.all_quizzes_completed.extend(progress.get_completed_quiz())


class Educator(User):
    def __init__(self, id, firstname, lastname, username, email, password):
        super().__init__(id, firstname, lastname, username, email, password)
    

class Parent(User):
    def __init__(self, id, firstname, lastname, username, email, password):
        super().__init__(id, firstname, lastname, username, email, password)
