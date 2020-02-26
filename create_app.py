from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile("settings.py")

db = SQLAlchemy(app)

def create_app():

    db.init_app(app)

    # import the apps
    from admin.views import admin_app
    from cart.views import cart_app
    from checkout.views import checkout_app
    from home.views import home_app
    from order.views import order_completion_app
    from product.views import product_app

    # Register the app
    app.register_blueprint(admin_app)
    app.register_blueprint(cart_app)
    app.register_blueprint(checkout_app)
    app.register_blueprint(home_app)
    app.register_blueprint(product_app)
    app.register_blueprint(order_completion_app)

    return app