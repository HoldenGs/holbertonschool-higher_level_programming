#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    url = 'https://swapi.co/api/people/?search={}'.format(argv[1])
    r = requests.get(url).json()
    results = r['results']
    people = '\n'.join(list(person['name'] for person in results))
    print('Number of result: {}\n{}'.format(r['count'], people))
