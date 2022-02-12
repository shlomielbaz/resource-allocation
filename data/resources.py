#!/usr/bin/env python3

from data import engine, session, Resource
from sqlalchemy import Sequence


def get_resources(filters: dict = None):
    # session.query(User).all()
    if filters is None:
        data = session.query(Resource).all()
    else:
        data = session.query(Resource).filter_by(**filters).fetchall()

    return data


def get_resource(filters: dict):
    query = session.query(Resource).filter_by(**filters)

    return query.first()


def set_resource(resource: object, data: dict):
    for key, value in data.items():
        if hasattr(resource, key):
            setattr(resource, key, value)

    return session.commit()


def add_resource(data: dict):
    resource = Resource(data)
    session.add(resource)

    return session.commit()


def del_resource(resource: object):
    session.delete(resource)

    return session.commit()
