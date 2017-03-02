#!/usr/bin/python3

"""
List all items in a states table in a database
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user='%s'.format(argv[1]),
                         passwd='%s'.format(argv[2]), db='%s'.format(argv[3]))
    c = db.cursor()
    c.execute("""SELECT id, name FROM states ORDER BY states.id ASC""")
