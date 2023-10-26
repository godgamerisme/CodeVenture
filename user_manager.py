from database.UserDatabase import UserDatabase

class UserManager:
    """
     A singleton instance to manage all users
    """
    __instance = None

    @staticmethod
    def get_instance():
        """
        Static access method
        """
        if UserManager.__instance == None:
            UserManager()
        return UserManager.__instance

    def __init__(self):
        """
        Virtually private constructor
        """
        if UserManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            UserManager.__instance = self
            self.user_db = UserDatabase("./data/users.json")
            self.users = self.user_db.get_user_array()

    def get_user_db(self):
        """
        Get the user database
        """
        return self.user_db

    def get_all_users(self):
        """
        Get all users
        """
        return self.users

    def get_user(self, user_id):
        """
        Get a user by its id
        """
        for user in self.users:
            if user.get_user_id() == user_id:
                return user
        return None

    def get_user_by_username(self, username):
        """
        Get a user by its username
        """
        for user in self.users:
            if user.get_username() == username:
                return user
        return None
    
    def get_user_fullname(self, user_id):
        """
        Get a user's full name by its id
        """
        for user in self.users:
            if user.get_user_id() == user_id:
                return user.get_fullname()
        return None

    def get_all_young_learners(self):
        """
        Get all young learners
        """
        return [user for user in self.users if user.get_usertype() == "younglearner"]
    