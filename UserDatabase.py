import json

class JsonDatabase:
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

if __name__ == "__main__":
    db = JsonDatabase("./data/users.json")
    data = db.read_data()
    print(data)