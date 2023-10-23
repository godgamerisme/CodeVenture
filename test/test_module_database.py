import json
from database.ModuleDatabase import ModuleDatabase


"""
To run this test, run the following command in the terminal:
python pytest test/test_module_database.py
"""

# Test the ModuleDatabase class

def test_read_data_file_not_found(tmp_path):
    # Test when the file is not found
    db = ModuleDatabase(tmp_path / "non_existent_file.json")
    data = db.read_data()
    assert data == []

def test_read_data_file_found(tmp_path):
    # Test when the file is found
    data_to_write = {"key": "value"}
    file_path = tmp_path / "test_data.json"
    with open(file_path, 'w') as file:
        json.dump(data_to_write, file)

    db = ModuleDatabase(file_path)
    data = db.read_data()
    assert data == data_to_write

def test_write_data(tmp_path):
    # Test writing data to a file
    data_to_write = {"key": "value"}
    file_path = tmp_path / "test_data.json"

    db = ModuleDatabase(file_path)
    db.write_data(data_to_write)

    with open(file_path, 'r') as file:
        data = json.load(file)
    assert data == data_to_write

def test_to_module_array(tmp_path):
    # Test converting data to Module objects
    data_to_convert ={
        "modules": [
            {
                "module_id": 1,
                "module_name": "Module 1",
                "tutorials": [
                    {
                    "tutorial_id": 101,
                    "title": "Tutorial 1.1",
                    "content": "This is the content of Tutorial 1.1",
                    "duration_minutes": 10
                    },
                    {
                    "tutorial_id": 102,
                    "title": "Tutorial 1.2",
                    "content": "This is the content of Tutorial 1.2",
                    "duration_minutes": 15
                    },
                ],
                "quiz": {
                    "quiz_id": 101,
                    "title": "Quiz 1",
                    "questions": [],
                },
            },
            {
                "module_id": 2,
                "module_name": "Module 2",
                "tutorials": [],
                "quiz": {
                    "quiz_id": 101,
                    "title": "Quiz 2",
                    "questions": [],
                },
            },
        ],
        "users": [
            {
                "user_id": 1,
                "username": "user1",
                "module_progress": [
                    {
                        "module_id": 1,
                        "completed_tutorials": [101],
                        "completed_quiz": [301],
                    },
                    {
                        "module_id": 2,
                        "completed_tutorials": [201],
                        "completed_quiz": [302],
                    },
                ],
            },
        ],
    }

    file_path = tmp_path / "test_data.json"
    with open(file_path, 'w') as file:
        json.dump(data_to_convert, file)

    db = ModuleDatabase(file_path)
    modules = db.to_module_array(db.read_data())
    #Returned Module objects should have the correct module_id and module_name
    # Assert that the expected modules are in the result
    assert len(modules) == 2
    assert modules[0].module_id == 1
    assert modules[0].module_name == "Module 1"
    assert len(modules[0].tutorials) == 2
    assert modules[0].tutorials[0].tutorial_id == 101
    assert modules[0].tutorials[0].title == "Tutorial 1.1"
    assert modules[0].tutorials[0].content == "This is the content of Tutorial 1.1"
    assert modules[0].tutorials[0].duration_minutes == 10
    assert modules[0].quiz.quiz_id == 101

    assert modules[1].module_id == 2
    assert modules[1].module_name == "Module 2"
    assert len(modules[1].tutorials) == 0
    assert modules[1].quiz.quiz_id == 101

    # Assert that user progress data is correctly associated with modules
    user1_progress = modules[0].user_progress[0]  # User 1's progress for Module 1
    assert user1_progress.user_id == 1
    assert user1_progress.username == "user1"
    assert user1_progress.module_id == 1
    assert user1_progress.completed_tutorials == [101]
    assert user1_progress.completed_quiz == [301]