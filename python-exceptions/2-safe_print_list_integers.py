#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    _i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except TypeError:
            pass
        except ValueError:
            pass
        _i += 1
    print()
    return count
