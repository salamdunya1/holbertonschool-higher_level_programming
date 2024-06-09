#!/usr/bin/python3
"""defines a student JSON"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """defines a student"""
        if attrs is None:
            return vars(self)
        else:
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
