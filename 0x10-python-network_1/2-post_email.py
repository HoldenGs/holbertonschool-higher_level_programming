#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    from urllib import request, parse
    data = parse.urlencode({'email': argv[2]})
    data = data.encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
