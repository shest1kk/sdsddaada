from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

metadata = MetaData()

roles = Table('roles',
              metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String, nullable=False),
              Column('permissions', JSON))

users = Table('users',
              metadata,
              Column('id', Integer, primary_key=True),
              Column('username', String, nullable=False),
              Column('email', String, nullable=False),
              Column('phone', Integer, primary_key=True),
              Column('password', String, nullable=False),
              Column('registered_at', TIMESTAMP, default=datetime.utcnow),
              Column('trip_count', Integer, default=0),
              Column('role', Integer, ForeignKey('roles.id'))
              )

cars = Table('cars',
             metadata,
             Column('brand', String, nullable=False),
             Column('model', String, nullable=False),
             Column('plate', String, primary_key=True, nullable=False),
             Column('color', String, nullable=False,),
             Column('available', Boolean, default=True),
             Column('price', Integer, nullable=False),
             )

