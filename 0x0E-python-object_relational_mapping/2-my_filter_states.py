#!/usr/bin/python3

"""
List all items in a states table in a database
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT id, name FROM states WHERE name LIKE %s
    ORDER BY states.id ASC""", (argv[4],))
    for x in c.fetchall():
        print(x)
