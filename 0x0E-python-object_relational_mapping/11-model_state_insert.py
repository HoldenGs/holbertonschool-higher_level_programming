#!/usr/bin/python3

"""
Add a state called 'Louisiana' to the database
"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name='Louisiana'))
    state = session.query(State).filter(State.name == 'Louisiana')
    try:
        print(state[0].id)
        session.commit()
    except IndexError:
        print("Not found")
