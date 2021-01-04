from data.db import Base
import sqlalchemy as sa

class Name(Base):
    __tablename__ = 'names'

    id = sa.Column(sa.Integer, primary_key=True)
    the_name = sa.Column(sa.String(100), nullable=False)


    def __repr__(self):
        return self.the_name

    
    def to_dict(self):
        return {'name': self.the_name}