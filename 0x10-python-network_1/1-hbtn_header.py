#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    from urllib import request
    _, headers = request.urlretrieve(argv[1])
    print(headers['X-Request-Id'])
