#!/usr/bin/python3
"File reading"


def read_file(filename=""):
    "Prototype function for reading"

    with open(filename, "r") as f:
        print(f.read(), end="")
