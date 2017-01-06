#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length > 2:
        print("{:d} arguments:".format(length - 1))
        for i in range(1, length):
            print("{:d}: {:s}".format(i, argv[i]))
    elif length == 2:
        print("{:d} argument:\n{:d}: {:s}".format(1, 1, argv[1]))
    else:
        print("0 argument.")
