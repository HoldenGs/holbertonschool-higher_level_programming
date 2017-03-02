#!/usr/bin/python3

"""
List all items in a states table in a database
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    keywords = argv[4].split(';', 1)
    c.execute("""SELECT name
    FROM cities
    WHERE state_id = (SELECT id FROM states WHERE name = '{}')
    ORDER BY cities.id ASC""".format(keywords[0].strip("'")))
    print(', '.join(city[0] for city in c.fetchall()))
