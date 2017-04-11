#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    from urllib import request, error
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.URLError as e:
        print('Error code: {}'.format(e.code))
