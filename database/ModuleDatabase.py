import json
from Modules import *
from typing import List

class ModuleDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_data()
        self.module_array = self.to_module_array()

    def get_data(self):
        return self.data

    def get_module_array(self)->List[Module]:
        return self.module_array

    def read_data(self):
        """
        Reads data from json file
        :return: data read from json
        :returntype: dict or empty list
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return []

    def write_data(self):
        """
        Writes data to json file
        :param data: data to write to json
        :return: None
        """
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_user_module_progress(self,user_id):
        """
        Return the reference to the database entry of the user's module progress
        """
        for user in self.data["users"]:
            if user["user_id"] == user_id:
                return user["module_progress"]
        return None

    def to_module_array(self)->List[Module]:
        """
        Converts the data from json to an array of Module objects
        :param data: data read from json
        :return: array of Module objects
        """
        modules = [Module(**module_data) for module_data in self.data["modules"]]
        users = self.data.get("users", [])
        for user_data in users:
            user_id = user_data["user_id"]
            username = user_data["username"]
            
            module_progress_data = user_data.get("module_progress", [])
            
            # Iterate through module progress data for each user
            for progress_item in module_progress_data:
                
                # Use **progress_item to directly unpack the data into Progress class
                progress = Progress(user_id, username, **progress_item)
                
                # Find the corresponding module
                module = next((module for module in modules if module.module_id == progress.module_id), None)
                
                # If the module exists, add the progress to the module
                if module:
                    module.add_user_progress(progress)

        return modules
 
    def complete_tutorial(self,user_id,module_id,tutorial_id):
        """
        Complete a tutorial
        """
        #Add tutorial id to the user's module progress in module array
        #Adding to the array will automatically update the data in json
        for module in self.module_array:
            if module.get_module_id() == module_id:
                for progress in module.get_user_progress():
                    if progress.get_user_id() == user_id:
                        progress.add_completed_tutorial(tutorial_id)
                        break
                break
        #Write data to json
        self.write_data()

    def complete_quiz(self,user_id,module_id,quiz_id):
        """
        Complete a quiz
        """
        #Add quiz id to the user's module progress in module array
        #Adding to the array will automatically update the data in json
        for module in self.module_array:
            if module.get_module_id() == module_id:
                for progress in module.get_user_progress():
                    if progress.get_user_id() == user_id:
                        progress.add_completed_quiz(quiz_id)
                        break
                break
        #Write data to json
        self.write_data()
        
    

if __name__ == "__main__":
    db = ModuleDatabase("./data/modules.json")
    data = db.read_data()
    modules = db.to_module_array(data)
    # print(modules)
    for module in modules:
        print(module)
        for tutorial in module.tutorials:
            print(tutorial)
        print(module.quiz)
        for question in module.quiz.questions:
            print(question)
            for option in question.options:
                print(option)
        for progress in module.user_progress:
            print(progress)
