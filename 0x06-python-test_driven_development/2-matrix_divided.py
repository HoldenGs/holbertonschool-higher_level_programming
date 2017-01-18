#!/usr/bin/python3
"""
2-matrix_divided

1 Function:
matrix_divided
"""
def matrix_divided(matrix, div):
    """
    matrix_divided: divided all elements of a matrix
    matrix: matrix to divid
    div: divisor

    exceptions:
    TypeError: non-integer/float values in matrix, rows w/ different sizes
    non-integer/float values in div

    ZeroDivisionError: div is 0
    """
    try:
        len_of_last = len(matrix[0])
        for i in matrix:
            if len(i) != len_of_last:
                raise TypeError("Each row of the matrix must have the same size")
            else:
                len_of_last = len(i)
            for j in i:
                if isinstance(j, (int, float)) is False:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if isinstance(div, (int, float)) is False:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        new_list = []
        for i in matrix:
            l = []
            for j in i:
                l.append(round(j / div, 2))
            new_list.append(l)
        return new_list
    except:
        raise
