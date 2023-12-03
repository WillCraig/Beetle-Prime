import datetime

from modules.globals import db


# -------------------------------------------------------------------------------------------------------

# Customer Model

class Customer(db.Model):
    """
    The Customer model represents a customer in the database.

    Attributes:
        customer_id (int): The primary key for the customer, auto-incremented.
        username (str): The username of the customer.
        password (str): The password of the customer.
        email (str): The email of the customer.
        street (str): The street address of the customer.
        city (str): The city of the customer.
        state (str): The state of the customer.
        zipcode (int): The zipcode of the customer.
    """
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)


# Product Model
class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.seller_id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    price = db.Column(db.DECIMAL(8, 2), nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    seller = db.relationship('Seller', backref=db.backref('products', lazy=True))
    img_link = db.Column(db.String(255), nullable=False)


# Order Model
class Order(db.Model):
    #
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))


# OrderProduct Model
class OrderProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order = db.relationship('Order', backref=db.backref('order_products', lazy='dynamic'))
    product = db.relationship('Product', backref=db.backref('order_products', lazy='dynamic'))

    @classmethod
    def add_product_to_order(cls, order_id, product_id, quantity):
        order_product = cls(order_id=order_id, product_id=product_id, quantity=quantity)
        db.session.add(order_product)
        db.session.commit()
        return order_product


# Seller Model
class Seller(db.Model):
    seller_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)


# Purchase Model
class Purchase(db.Model):
    purchase_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    purchase_date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)

    def __init__(self, order):
        self.customer_id = order.customer_id
        self.order_date = order.order_date


# PurchaseProduct Model
class PurchaseProduct(db.Model):
    __tablename__ = 'purchase_products'
    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase.purchase_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product', backref=db.backref('purchase_products', lazy='dynamic'))
    purchase = db.relationship('Purchase', backref=db.backref('purchase_products', lazy='dynamic'))

