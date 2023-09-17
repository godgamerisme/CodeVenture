import json
from os import path


def register():
    filename = 'C:\Users\Kelvin\OneDrive - Monash University\Y1S2\FIT1008 intro to comp sc\Github\FIT 1055 A3\CodeVenture\data\users.json'
    listObj = []
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
    
    # Read JSON file
    with open(filename) as fp:
        listObj = json.load(fp) 
    
    # Verify existing list
    print(listObj)
    print(type(listObj))
    
    # listObj.append({
    # "id": 1,
    # "firstname": "John",
    # "lastname": "Doe",
    # "username": "johndoe",
    # "email": "john@example.com",
    # "usertype": "younglearner"
    # })
    
    # Verify updated list
    print(listObj)
    
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '))
    
    print('Successfully appended to the JSON file')
    return "Successfully Registered"

if __name__ == "__main__":
    register()