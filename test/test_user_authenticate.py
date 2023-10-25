#Import UserAuthenticate class
from authentication.UserAuthenticate import UserAuthenticate
#Import UserDatabase class
from database.UserDatabase import UserDatabase
#Import User class
from User import *
import pytest

"""
To run this test, run the following command in the terminal:
python pytest test/test_user_authenticate.py
"""

def test_validate_name():
    db = UserDatabase("./test_users.json")
    # Create an instance of UserAuthenticate with sample data
    user_authenticate = UserAuthenticate(db=db, data_obj=[], users_array=[])

    # Valid name
    assert user_authenticate.validate_name("John") is True  
    assert user_authenticate.validate_name("Alice") is True  # Valid name

    # Invalid name
    assert user_authenticate.validate_name("123John") is False  
    assert user_authenticate.validate_name("NameIsTooLong") is False  # Invalid name

def test_validate_password():
    db = UserDatabase("./test_users.json")
    # Create an instance of UserAuthenticate with sample data
    user_authenticate = UserAuthenticate(db=db, data_obj=[], users_array=[])

    # Valid password
    assert user_authenticate.validate_password("Pass5") is True  
    assert user_authenticate.validate_password("StrongPassword") is True  # Valid password
    
    # Invalid password (too short)
    assert user_authenticate.validate_password("Pwd") is False  
    # Invalid password (too long)
    assert user_authenticate.validate_password("VeryLongPassword12345") is False  

def test_validate_usertype():
    db = UserDatabase("./test_users.json")
    # Create an instance of UserAuthenticate with sample data
    user_authenticate = UserAuthenticate(db=db, data_obj=[], users_array=[])

    assert user_authenticate.validate_usertype("younglearner") is True  # Valid usertype
    assert user_authenticate.validate_usertype("educator") is True  # Valid usertype
    assert user_authenticate.validate_usertype("parent") is True  # Valid usertype
    assert user_authenticate.validate_usertype("random") is False  # Invalid usertype

def test_validate_email():
    user_authenticate2 = UserAuthenticate(db=None, data_obj=[], users_array=[])

    # Mock the 'users' list with some sample users
    user1 = User(1, "John", "Doe", "jodo", "jodo0001@hotmail.com", "blabla")
    user2 = User(2, "Jane", "Smith", "jasm2", "jasm0002@gmail.com", "jane123")
    user_authenticate2.users = [user1, user2]

     # Test a valid and unique email
    assert user_authenticate2.validate_email("newuser@example.com") is True  # Valid email
    assert user_authenticate2.validate_email("blabla@gmail.com") is True  # Valid email

    # Test an empty email
    assert user_authenticate2.validate_email("") is False  # Invalid email (empty)

    # Test a non-unique email
    assert user_authenticate2.validate_email("jodo0001@hotmail.com") is False  # Invalid email (already exists)
    assert user_authenticate2.validate_email("jasm0002@gmail.com") is False  # Invalid email (already exists)

    #Test invalid email format
    assert user_authenticate2.validate_email("johndoe.com") is False  # Invalid email format
    assert user_authenticate2.validate_email("johndoe@example") is False  # Invalid email format

def test_register():
    db = UserDatabase("./test_users.json")
    user_authenticate3 = UserAuthenticate(db=db, data_obj=[], users_array=[])

    # Mock the 'users' list with some sample users
    user1 = User(1, "John", "Doe", "jodo", "jodo0001@hotmail.com", "blabla")
    user2 = User(2, "Jane", "Smith", "jasm2", "jasm0002@gmail.com", "jane123")
    user_authenticate3.users = [user1, user2]

    # Test valid registration
    # assert user_authenticate3.register("John", "Doe", "password123", "johndoe@example.com", "younglearner") is True
    # assert user_authenticate3.register("jane", "lol", "janelol", "jane@gmail.com", "educator") is True
    # assert user_authenticate3.register("Alice", "Smith", "alice123", "alice@hotmail.com", "parent") is True

    assert isinstance(user_authenticate3.register("John", "Doe", "password123", "johndoe@example.com", "younglearner"),YoungLearner) is True
    assert isinstance(user_authenticate3.register("jane", "lol", "janelol", "jane@gmail.com", "educator"),Educator) is True
    assert isinstance(user_authenticate3.register("Alice", "Smith", "alice123", "alice@hotmail.com", "parent") ,Parent) is True

    # Test registration with invalid input
    assert user_authenticate3.register("123John", "Doe", "password123", "johndoe@example.com", "younglearner") is False
    assert user_authenticate3.register("John", "Doe", "pwd", "johndoe@example.com", "younglearner") is False

    # Test registration with duplicate email
    assert user_authenticate3.register("John", "Doe", "password123", "jodo0001@hotmail.com", "younglearner") is False
    assert user_authenticate3.register("Jane", "Smith", "password123", "jasm0002@gmail.com","educator") is False

def test_login():
    db = UserDatabase("./test_users.json")
    # Create an instance of UserAuthenticate with sample data
    user_authenticate = UserAuthenticate(db=db, data_obj=[], users_array=[])

    # Mock the 'users' list with some sample users
    user1 = User(1, "John", "Doe", "jodo", "jodo0001@hotmail.com", "blabla")
    user2 = User(2, "Jane", "Smith", "jasm2", "jasm0002@gmail.com", "jane123")
    user_authenticate.users = [user1, user2]

    # Test valid login
    assert user_authenticate.login("jodo", "blabla") == user1
    assert user_authenticate.login("jasm2", "jane123") == user2

    # Test login with invalid username
    assert user_authenticate.login("jane", "jane123") is False
    assert user_authenticate.login("Jodo", "blabla") is False

    # Test login with invalid password
    assert user_authenticate.login("jodo", "password123") is False
    assert user_authenticate.login("jasm2", "Jane123") is False

    # Test login with empty username
    assert user_authenticate.login("", "blabla") is False

    # Test login with empty password
    assert user_authenticate.login("jodo", "") is False

def test_reset_password():
    db = UserDatabase("./test_users.json")
    # Create an instance of UserAuthenticate with sample data
    user_authenticate = UserAuthenticate(db=db, data_obj=[], users_array=[])

    # Mock the 'users' list with some sample users
    user1 = User(1, "John", "Doe", "jodo", "jodo0001@hotmail.com", "blabla")
    user2 = User(2, "Jane", "Smith", "jasm2", "jasm0002@gmail.com", "jane123")
    user_authenticate.users = [user1, user2]

    # Test valid reset password
    assert user_authenticate.reset_password("jodo0001@hotmail.com", "newpassword") is True
    assert user_authenticate.reset_password("jasm0002@gmail.com", "newpassword") is True

    # Test reset password with invalid username
    assert user_authenticate.reset_password("jane@hotmail.com", "newpassword") is False
    assert user_authenticate.reset_password("Jodo0001@hotmail.com", "newpassword") is False

    # Test reset password with empty username
    assert user_authenticate.reset_password("", "newpassword") is False

    # Test reset password with empty password
    assert user_authenticate.reset_password("jodo0001@hotmail.com", "") is False

    # Test reset password with invalid password
    assert user_authenticate.reset_password("jodo0001@hotmail.com", "pwd") is False
    assert user_authenticate.reset_password("jodo0001@hotmail.com", "verylongpassword12345") is False




    