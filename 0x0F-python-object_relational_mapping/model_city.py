#!/usr/bin/python3
"""
Module that connect a database
with port 3306 and create table
as syntax of SQLalchemy
"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from model_state import Base


class City(Base):
    """ inherits"""
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False, )
