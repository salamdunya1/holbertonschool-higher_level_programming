#!/usr/bin/python3
"Write in file"


def write_file(filename="", text=""):
    "writes a string to a text file"
    with open(filename, "w") as f:
        return f.write(text)
