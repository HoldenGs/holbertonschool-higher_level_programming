#!/usr/bin/python3

"""
List all items in a states table in a database
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC""")
    for x in c.fetchall():
        print(x)
