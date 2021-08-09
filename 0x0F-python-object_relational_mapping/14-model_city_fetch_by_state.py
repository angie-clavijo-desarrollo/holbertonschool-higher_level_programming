#!/usr/bin/python3
"""
Module for connecting to SQLalquemy database
and view the arguments of the database
and doing query at database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    city = session.query(State, City).join(City).order_by(City.id)
    for state, city in city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()