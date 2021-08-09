#!/usr/bin/python3
"""
Module for connecting to SQLalquemy database
and view the arguments of the database
and doing query at database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

# expression not execute when load
if __name__ == "__main__":

    # to connect
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # configuration session
    Session = sessionmaker(bind=engine)

    # created session with constructor:
    session = Session()

    Base.metadata.create_all(engine)
    results = session.query(State).filter(State.name == argv[4]).first()

    if results:
        print("{}".format(results.id))
    if results in None:
        print("Not found")
    session = session.close()
