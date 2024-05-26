#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
<<<<<<< HEAD
        for num in row:
            print("{:d}".format(num))
=======
        for i, num in enumerate(row):
            print("{:d}".format(num), end="")
            if i < len(row) - 1:
                print(" ", end="")
>>>>>>> refs/remotes/origin/main
        print()
