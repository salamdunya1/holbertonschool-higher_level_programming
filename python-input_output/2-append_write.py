#!/usr/bin/python3
"""Append to the file"""


def append_write(filename="", text=""):
    """append to the file"""
    with open(filename, "a") as f:
        return f.write(text)
