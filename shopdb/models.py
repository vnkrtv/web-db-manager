from datetime import datetime
from shopdb import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    customers = db.relationship('Customer', backref='user', uselist=False)
    workers = db.relationship('Worker', backref='user', uselist=False)
    suppliers = db.relationship('Supplier', backref='user', uselist=False)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    warehouses = db.relationship('Warehouse', backref='product', uselist=False)
    suppliers = db.relationship('Supplier', backref='product')
    orders = db.relationship('Order', backref='product')
    deliveries = db.relationship('Delivery', backref='product')

    def __repr__(self):
        return '<Product: {}>'.format(self.name)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(32), nullable=False)
    country = db.Column(db.String(32), nullable=False)
    postal_code = db.Column(db.String(16), index=True, unique=True, nullable=False)
    customers = db.relationship('Customer', backref='address')
    suppliers = db.relationship('Supplier', backref='address')

    def __repr__(self):
        return '<Address: {}({})>'.format(self.city, self.postal_code)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True, unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    first_name = db.Column(db.String(16), nullable=False)
    second_name = db.Column(db.String(16), nullable=False)
    orders = db.relationship('Order', backref='customer')

    def __repr__(self):
        return '<Customer: {} {}>'.format(self.first_name, self.second_name)


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    name = db.Column(db.String(128))
    deliveries = db.relationship('Delivery', backref='supplier')

    def __repr__(self):
        return '<Supplier: {}(product_id={})>'.format(self.name, self.product_id)


class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    first_name = db.Column(db.String(16), nullable=False)
    second_name = db.Column(db.String(16), nullable=False)
    salary = db.Column(db.Integer)
    position = db.Column(db.String(32))

    def __repr__(self):
        return '<Worker: {} {}>'.format(self.first_name, self.second_name)


class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Warehouse: {}({})>'.format(self.product_id, self.quantity)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Order: product(id={}) to customer(id={}))>'.format(self.product_id, self.customer_id)


class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Delivery: product(id={}) from supplier(id={})>'.format(self.product_id, self.supplier_id)
