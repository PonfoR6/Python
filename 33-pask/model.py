from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

    cars = relationship('Car', back_populates='owner')


class PostSettings(Base):
    __tablename__ = 'postsettings'

    id = Column(Integer, primary_key=True, index=True)
    consumption = Column(Integer)
    mileage = Column(Integer)

    car = relationship('Car', back_populates='settings', uselist=False)


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)

    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='cars')

    settings_id = Column(Integer, ForeignKey('postsettings.id'))
    settings = relationship('PostSettings', back_populates='car')
