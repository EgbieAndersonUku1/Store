from create_app import db


class AdminLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(5))
    password = db.Column(db.String(255))