from data.db import session

from ..models.names import Name

def get_all_names():
    return session.query(Name).all()