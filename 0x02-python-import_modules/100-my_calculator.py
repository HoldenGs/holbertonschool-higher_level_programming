#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    op = int(argv[2])
    b = int(argv[3])
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
