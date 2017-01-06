#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = argv[1]
    op = argv[2]
    b = argv[3]
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
