import os
import re
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, Resource

VALID_TAG = re.compile(r'^[a-z0-9]+$')


def _create_session():
    db_url = os.environ.get('DATABASE_URL')
    __dir = f"{os.path.dirname(__file__)}\\.."
    path = os.path.abspath(__dir)

    db_url = f'sqlite:///{path}\\data\\db.sqlite'

    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    return create_session()


session = _create_session()


def truncate_tables():
    session.commit()


def get_resources():
    return session.query(Resource).order_by(Resource.name.asc()).all()


def add_resource(data: dict):
    # for tag, count in hashtags_cnt.items():
    session.add(Resource(data))
    session.commit()

