#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        string = " ".join([format(x) for x in i])
        print(string)
