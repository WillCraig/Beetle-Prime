# FOLLOWING LINES ARE PASTED FOR DEVELOPMENT
# CODE WILL NEED TO BE MOVED TO app.py FOR USE.

from flask import Flask, redirect, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'annoying'
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="root",password="",hostname="localhost",databasename="testDB",)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Customer Model
class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)

# Order Model
class Order(db.Model):
    order_num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    order_quantity = db.Column(db.Integer, nullable=False)
    order_status = db.Column(db.String(255), nullable=False)
    price_total = db.Column(db.Integer, nullable=False)
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))

# Order_Items Model
class OrderItems(db.Model):
    order_num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(50), nullable=False)
    order = db.relationship('Order', backref=db.backref('items', lazy=True))

# Product Model
class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.seller_id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    price = db.Column(db.DECIMAL(8, 2), nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    seller = db.relationship('Seller', backref=db.backref('products', lazy=True))

# Product_Image Model
class ProductImage(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_url = db.Column(db.String(50), nullable=False)
    product = db.relationship('Product', backref=db.backref('images', lazy=True))

# Purchase Model
class Purchase(db.Model):
    order_num = db.Column(db.Integer, db.ForeignKey('order.order_num'), nullable=False, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False, primary_key=True)
    order = db.relationship('Order', backref=db.backref('purchases', lazy=True))
    product = db.relationship('Product', backref=db.backref('purchases', lazy=True))

# Seller Model
class Seller(db.Model):
    seller_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)


# create the tables.
db.create_all()