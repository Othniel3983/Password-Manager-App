import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return{}
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_credentials(website, username, password):
    data = load_data()
    data[website] = {"username": username, "password": password}
    save_data(data)

def get_credentials(website):
    data = load_data()
    return data.get(website, None)

def delete_credentials(website):
    data = load_data()
    if website in data:
        del data[website]
        save_data(data)
        return True
    return False


