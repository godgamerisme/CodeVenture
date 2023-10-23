import pytest
import os
from database.UserDatabase import UserDatabase
import json
from User import YoungLearner, Educator, Parent

"""
To run this test, run the following command in the terminal:
python pytest test/test_user_database.py
"""

# Define a temporary JSON file path for testing
TEST_JSON_FILE = "test_users.json"

# Sample user data to use in tests
sample_user_data = [
    {
        "id": 1,
        "firstname": "John",
        "lastname": "Doe",
        "username": "johndoe",
        "email": "john@example.com",
        "password": "password123",
        "usertype": "younglearner"
    },
    {
        "id": 2,
        "firstname": "Alice",
        "lastname": "Smith",
        "username": "alicesmith",
        "email": "alice@example.com",
        "password": "securepass",
        "usertype": "educator"
    },
    {
        "id": 3,
        "firstname": "Bob",
        "lastname": "Johnson",
        "username": "bobjohnson",
        "email": "bob@example.com",
        "password": "pass1234",
        "usertype": "parent"
    }
]

@pytest.fixture
def user_db():
    # Create a temporary JSON file with sample user data for testing
    with open(TEST_JSON_FILE, "w") as file:
        json.dump(sample_user_data, file)

    db = UserDatabase(TEST_JSON_FILE)
    yield db

    # Clean up after the tests by removing the temporary JSON file
    os.remove(TEST_JSON_FILE)

def test_read_data(user_db):
    # The read_data method should return the sample user data
    data = user_db.read_data()
    assert data == sample_user_data

def test_write_data(user_db):
    new_user_data = [
        {
            "id": 4,
            "firstname": "Eva",
            "lastname": "Williams",
            "username": "evawilliams",
            "email": "eva@example.com",
            "password": "evapassword",
            "usertype": "younglearner"
        }
    ]

    # Write new user data to the JSON file
    user_db.write_data(new_user_data)

    # Read the data from the file to check if it was written correctly
    data = user_db.read_data()
    assert data == new_user_data

def test_to_user_array(user_db):
    # The to_user_array method should return a list of User objects
    users = user_db.to_user_array()

    assert isinstance(users, list)
    assert len(users) == len(sample_user_data)

    # Check if the returned user objects match the sample data
    for user, sample_data in zip(users, sample_user_data):
        assert user.id == sample_data["id"]
        assert user.firstname == sample_data["firstname"]
        assert user.lastname == sample_data["lastname"]
        assert user.username == sample_data["username"]
        assert user.email == sample_data["email"]
        assert user.password == sample_data["password"]
        assert user.usertype.lower() == sample_data["usertype"].lower()

    # Check if the returned user objects are of the correct type
    assert isinstance(users[0], YoungLearner)
    assert isinstance(users[1], Educator)
    assert isinstance(users[2], Parent)


