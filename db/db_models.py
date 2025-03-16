from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
import logging
from datetime import datetime

Base = declarative_base()


class Category(Base):
    """Sheet for products categories"""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    products = relationship('Product', back_populates='category')


class Product(Base):
    """Sheet for products"""
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    barcode = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')


class Sale(Base):
    """Sheet for sales"""
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    product = relationship('Product')


class User(Base):
    """Sheet for users"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
