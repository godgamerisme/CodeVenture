import json
from Modules import *

class ModuleDatabase:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return []

    def write_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def to_module_array(self, data):
        modules = [Module(**module_data) for module_data in data["modules"]]
        users = data.get("users", [])
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
    