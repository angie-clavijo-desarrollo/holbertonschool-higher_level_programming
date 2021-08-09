#!/usr/bin/python3
"""
Module that connect a database
with port 3306 and create table
as syntax of SQLalchemy
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
""" super class that permit of mapping of class children"""


class City(Base):
    """ inherits"""
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
