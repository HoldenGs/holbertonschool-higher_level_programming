#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    r = requests.get(argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
