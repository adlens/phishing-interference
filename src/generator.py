import json


def load_credentials(file_path):
    with open(file_path, "r") as file:
        credentials = json.load(file)
    return [(entry["email"], entry["password"]) for entry in credentials]
