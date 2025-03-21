from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
import logging
from datetime import datetime

Base = declarative_base()

order_items = Table(
    'order_items',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True),
    Column('quantity', Integer, nullable=False)
)


class Category(Base, AsyncAttrs):
    """Sheet for products categories"""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    products = relationship('Product', back_populates='category')

    def __repr__(self):
        return f'<Category(name={self.name})>'


class Product(Base, AsyncAttrs):
    """Sheet for products"""
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    barcode = Column(String, unique=True, nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')
    orders = relationship('Order', secondary=order_items, back_populates='products')

    def __repr__(self):
        return f'<Product(name={self.name}, barcode={self.barcode})>'


class Sale(Base, AsyncAttrs):
    """Sheet for sales"""
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    product = relationship('Product')


class User(Base, AsyncAttrs):
    """Sheet for users"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)


class Order(Base, AsyncAttrs):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    number = Column(String(11), unique=True, nullable=False)
    client = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False, default='Створено')
    date = Column(DateTime, default=datetime.utcnow)
    manager = Column(String(255), nullable=True)
    comment = Column(String(1024), nullable=True)
    payment = Column(String(50), nullable=True)
    end_date = Column(DateTime, nullable=True)
    total_amount = Column(Float, nullable=True)
    products = relationship('Product', secondary=order_items, back_populates='orders')


    def __repr__(self):
        return f'<Order(number={self.number}, client={self.client}, status={self.status})>'
