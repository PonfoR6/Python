from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)

    setting = relationship("Settings", back_populates="user", uselist=False)

    car = relationship("Car", back_populates="user")


class Settings(Base):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True, index=True)
    distance = Column(String)
    consumption = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="setting")


class Model(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True, index=True)
    car_model = Column(String)

    car = relationship("Car", back_populates="model")


class Mileage(Base):
    __tablename__ = 'mileage'

    id = Column(Integer, primary_key=True, index=True)
    mileage_max = Column(Integer)

    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship('Car', back_populates='mileage')


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)

    car = relationship("Car", back_populates="brand")


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    color = Column(String)
    year = Column(Integer)

    brand_id = Column(Integer, ForeignKey('brands.id'))
    brand = relationship('Brand', back_populates='car')
    model_id = Column(Integer, ForeignKey('models.id'))
    model = relationship('Model', back_populates='car')
    users_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='car')

    mileage = relationship("Mileage", back_populates="car")
