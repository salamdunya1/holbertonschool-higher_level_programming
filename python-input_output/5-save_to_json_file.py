#!/usr/bin/python3
"""writes an Object"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
