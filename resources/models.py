from sqlalchemy import Column, Sequence, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Resource(Base):
    __tablename__ = 'resources'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(300), name="name", nullable=False)
    type = Column(String(10), name="type", default=text('server'))
    priority = Column(Integer, name="priority", nullable=False)

    def __repr__(self):
        return "<Tip('%d', '%s')>" % (self.id, self.name)
