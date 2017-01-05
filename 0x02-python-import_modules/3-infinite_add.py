#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    sum = 0
    if length > 2:
        for i in range(1, length):
            nextnum = int(argv[i])
            sum += nextnum
        print("{:d}".format(sum))
    else:
        print("Give me 2 or more numbers!")
