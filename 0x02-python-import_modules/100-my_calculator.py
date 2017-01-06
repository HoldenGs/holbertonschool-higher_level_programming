#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = sys.argv[1]
    op = sys.argv[2]
    b = sys.argv[3]
    if op == '+':
        result = add(int(a), int(b))
    elif op == '-':
        result = sub(int(a), int(b))
    elif op == '*':
        result = mul(int(a), int(b))
    elif op == '/':
        result = div(int(a), int(b))
    else:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, result))
