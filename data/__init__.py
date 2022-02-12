from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from data.entities import Resource

import os

try:
    __dir = f"{os.path.dirname(__file__)}"
    __path = os.path.abspath(__dir)

    db_url = f'sqlite:///{__path}/db.sqlite'

    __engine = create_engine(db_url)
    __session = sessionmaker(bind=__engine)
    session = __session()
    connect = __engine.connect()
    engine = __engine
except Exception as e:
    exit(1)
