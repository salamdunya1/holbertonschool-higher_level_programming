#!/usr/bin/python3
"""Student JSON"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to json"""
        return vars(self)
