import json

def load_config():
    """Load credentials from cred.json"""
    with open("cred.json", "r") as file:
        return json.load(file)

config = load_config()
