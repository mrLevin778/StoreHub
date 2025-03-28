from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table, Enum, JSON
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.types import ARRAY
from sqlalchemy.ext.asyncio import AsyncAttrs
from enum import Enum as PyEnum
import logging
from datetime import datetime

Base = declarative_base()

order_items = Table(
    'order_items',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id'), primary_key=True),
    Column('goods_id', Integer, ForeignKey('goods.id'), primary_key=True),
    Column('quantity', Integer, nullable=False),
    Column('price', Float, nullable=False)
)


class OrderStatus(PyEnum):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    CANCELED = 'Canceled'
    REFUNDED = 'Refunded'


class PaymentMethod(PyEnum):
    CASH_PREPAYMENT = 'Cash Prepayment'
    CASH_ON_DELIVERY = 'Cash On Delivery'
    CARD_PREPAYMENT = 'Card Prepayment'
    CARD_ON_DELIVERY = 'Card On Delivery'
    OTHER = 'Other'


class Category(Base, AsyncAttrs):
    """Sheet for products categories"""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    products = relationship('Goods', back_populates='category')

    def __repr__(self):
        return f'<Category(name={self.name})>'


class Goods(Base, AsyncAttrs):
    """Sheet for goods"""
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String(100), unique=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    purchase_price = Column(Float, nullable=True)
    price = Column(Float, nullable=True)
    stock = Column(Integer, default=0)
    barcode = Column(String, unique=True, nullable=True)
    status = Column(String(50), nullable=False)
    rating = Column(Float, nullable=True)
    weight = Column(Float, nullable=True)
    dimensions = Column(String(100), nullable=True)
    discount = Column(Float, nullable=True)
    image_url = Column(String(255), nullable=True)
    tags = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='goods')
    supplier = relationship('Supplier', backref='goods')
    orders = relationship('Order', secondary=order_items, back_populates='goods')

    def __repr__(self):
        return f'<Goods(name={self.name}, barcode={self.barcode})>'


class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    contact_name = Column(String(255), nullable=True)
    contact_email = Column(String(255), nullable=True)
    contact_phone = Column(String(50), nullable=True)
    address = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    goods = relationship('Goods', backref='supplier', lazy='dynamic')

    def __repr__(self):
        return f'<Supplier(id={self.id}, name={self.name})>'


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
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(11), unique=True, nullable=False)
    customer = Column(String(255), nullable=True)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    manager = Column(String(255), nullable=True)
    comment = Column(String(1024), nullable=True)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    payment_status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    discount = Column(Float, default=0.0)
    tax = Column(Float, default=0.0)
    items = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    total_amount = Column(Float, nullable=False)
    products = relationship('Goods', secondary=order_items, back_populates='orders')
    order_type = Column(Enum('POS', 'Manager', 'Online', name='order_type_enum'), default='POS')

    def __repr__(self):
        return f'<Order(number={self.number}, customer={self.customer}, status={self.status}, total_amount={self.total_amount}, order_type={self.order_type})>'
