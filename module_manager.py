from database.ModuleDatabase import ModuleDatabase

class ModuleManager:
    """
    A singleton instance to manage all modules
    """
    __instance = None

    @staticmethod
    def get_instance():
        """
        Static access method
        """
        if ModuleManager.__instance == None:
            ModuleManager()
        return ModuleManager.__instance

    def __init__(self):
        """
        Virtually private constructor
        """
        if ModuleManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ModuleManager.__instance = self
            self.modules_db = ModuleDatabase("./data/modules.json")
            self.modules = self.modules_db.to_module_array()

    def get_module_db(self):
        """
        Get the module database
        """
        return self.modules_db

    def get_modules(self):
        """
        Get all modules
        """
        return self.modules

    def get_module(self, module_id):
        """
        Get a module by its id
        """
        for module in self.modules:
            if module.get_module_id() == module_id:
                return module
        return None
    
    def calculate_number_of_tutorials(self):
        """
        Calculate the number of tutorials in all modules
        """
        return sum([len(module.get_tutorials()) for module in self.modules])
    
    def calculate_number_of_quizzes(self):
        """
        Calculate the number of quizzes in all modules
        """
        return len(self.modules)    

    