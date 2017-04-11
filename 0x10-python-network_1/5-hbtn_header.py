#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])
