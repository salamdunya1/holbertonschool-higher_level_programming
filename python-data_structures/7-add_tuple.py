#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Assurer que chaque tuple a au moins 2 éléments
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    # Ajouter les éléments correspondants des deux tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
