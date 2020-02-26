from sqlalchemy.types import Float

from create_app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(3))
    first_name = db.Column(db.String(25))
    surname = db.Column(db.String(25))
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    phone_number = db.Column(db.Integer)
    state = db.Column(db.String(30))
    email = db.Column(db.String(50))
    country = db.Column(db.String(20))
    payment_type = db.Column(db.String(10))
    payment_status = db.Column(db.String(20))
    reference_num = db.Column(db.String(15))
    items = db.relationship("Order", backref="user", lazy=True)

    def __init__(self, reference_num=None):
        self.reference_num = reference_num


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)
    total_order = db.Column(Float)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    description = db.Column(db.String(500))
    image = db.Column(db.String(100))
    type = db.Column(db.String(25))
    live = db.Column(db.Boolean)
    orders = db.relationship('Order', backref='product', lazy=True)