from typing import List
from Modules import *
# from user_manager import UserManager

class User:
    def __init__(self, id, firstname, lastname, username, email, password, usertype):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.usertype = usertype

    def get_usertype(self):
        return self.usertype

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
    
    def get_fullname(self):
        return self.firstname + " " + self.lastname

    def __str__(self):
        return f"User: {self.id}, {self.firstname}, {self.lastname}, {self.username}, {self.email}, {self.password}"


class YoungLearner(User):
    def __init__(self, id, firstname, lastname, username, email, password, usertype):
        super().__init__(id, firstname, lastname, username, email, password, usertype)
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
    def __init__(self, id, firstname, lastname, username, email, password, usertype):
        super().__init__(id, firstname, lastname, username, email, password, usertype)
    

class Parent(User):
    def __init__(self, id, firstname, lastname, username, email, password, usertype, children:List[str]=[]):
        super().__init__(id, firstname, lastname, username, email, password, usertype)
        self.children = children

    def get_children(self):
        return self.children
    
    def add_child(self, child_email:str):
        if len(self.children)<2:
            if child_email not in self.children:
                self.children.append(child_email)
            else:
                return "Child already registered"
            return "Child added successfully"
        else:
            return "You have reached the maximum number of children"

   
