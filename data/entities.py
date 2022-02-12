# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Enum, Float, ForeignKey, SmallInteger, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Sequence, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Resource(Base):
    __tablename__ = 'resources'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(300), name="name", nullable=False)
    type = Column(String(10), name="type", default=text('server'))
    priority = Column(Integer, name="priority", nullable=False)
    is_occupied = Column(Integer, name="is_occupied", default=0)

    # def __repr__(self):
    #     return "<Resource('%d', '%s', '%s', '%d')>" % (self.id, self.name, self.type, self.priority)
    #     # return dict({
    #     #     'id': self.id, 'name': self.name, 'type': self.type, 'priority': self.priority
    #     # })

    def __init__(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
