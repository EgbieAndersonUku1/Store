from create_app import db
from utils.passwd import Password
from admin.model import AdminLogin



password  = "123456789"

admin = AdminLogin(user="admin", password=Password.hash_password(password))
db.session.add(admin)
db.session.commit()
