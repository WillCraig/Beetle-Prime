import sqlalchemy
from modules.globals import db
import datetime



# FIXME: make sure the datetime stuff is right.
# -------------------------------------------------------------------------------------------------------

# Customer Model
class Customer(db.Model):
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

# Order Model
class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))

# Association Table for Orders and Products (Many-to-Many Relationship)
class OrderProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product', backref=db.backref('order_products', lazy=True))
    order = db.relationship('Order', backref=db.backref('order_products', lazy=True))

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

class Purchase(db.Model):
    product_id_list = []
    purchase_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    # Add other fields as needed

    def __init__(self, order, product_id_list):
        self.customer_id = order.customer_id
        self.order_date = order.order_date
        self.product_id_list = product_id_list
        # Populate other fields as needed


# When the app starts, it will check if the user has an associated order (cart). if not, it will create one.

