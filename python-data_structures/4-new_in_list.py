#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Renvoie une copie de la liste originale
    else:
        new_list = my_list[:]  # Crée une copie de la liste originale
        new_list[idx] = element  # Remplace l'élément à l'index spécifié
        return new_list
