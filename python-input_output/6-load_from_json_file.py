#!/usr/bin/python3
"""creates an Object """


import json


def load_from_json_file(filename):
    """creates an Object """
    with open(filename) as f:
        return json.loads(f.read())
