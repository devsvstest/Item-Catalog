#!/usr/bin/env python3
# Item Catalog

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime


Base = declarative_base()


class Item_user(Base):
    __tablename__ = "itemuser"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(100), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):

        return {
            'name': self.name,
            'email': self.email,
            'id': self.id,
            'picture': self.picture
        }


class Catalog(Base):
    __tablename__ = "catalog"

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    category = Column(String(80))
    description = Column(String(250))
    created_datetime = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('itemuser.id'))
    itemuser = relationship(Item_user)

    @property
    def serialize(self):

        return {
            'title': self.title,
            'category': self.category,
            'id': self.id,
            'description': self.description,
            'created_datetime': self.created_datetime,
            'user_id': self.user_id
        }


engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)
