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
    c.execute("""SELECT id, name FROM states WHERE name REGEXP BINARY '{}' \
    ORDER BY states.id ASC""".format(keywords[0].strip("'")))
    for x in c.fetchall():
        print(x)
