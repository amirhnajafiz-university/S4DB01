"""
This file loads the json data queries to import template data
to our database.
"""
import json


PATH = './database/data.json'


def load_data():
    with open(PATH, 'r') as file:
        object = json.load(file)
        return object
