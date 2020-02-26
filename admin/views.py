from os.path import join
from time import time as time_stamp
from flask import Blueprint, session, url_for, render_template, flash, abort
from sqlalchemy import desc
from werkzeug.utils import redirect, secure_filename

from admin.form import AdminLoginForm
from admin.model import AdminLogin
from product.forms import ProductForm
from settings import UPLOAD_DIR
from user.models import Product, User, Order
from utils.decorators import is_user_already_logged_in, is_admin
from utils.is_url_safe import is_safe_url, if_url_is_safe_redirect
from utils.passwd import Password

from create_app import db

admin_app = Blueprint('admin_app', __name__, url_prefix="/admin")


_PER_PAGE = 16


@admin_app.route("/login", methods=["GET", "POST"])
@is_user_already_logged_in
def admin_login():
    form = AdminLoginForm()
    error = False

    if form.validate_on_submit():
        user = AdminLogin.query.filter_by(user="admin").first()

        if user and "admin" == form.username.data.lower() and Password.check_password(form.password.data, user.password):
            session["admin"] = "admin"
            return redirect(url_for("home_app.home"))

        error = True

    return render_template("admin/admin_login.html", form=form, error=error)


@admin_app.route('/add', methods=["GET", "POST"])
@is_admin
def add():

    form = ProductForm()

    if form.validate_on_submit():
        file_name = str(time_stamp()) + secure_filename(form.image.data.filename)
        img_path = join(UPLOAD_DIR, file_name)

        product = Product(name=form.name.data, price=form.price.data, stock=form.stock.data,
                          description=form.description.data, image=file_name, type=form.type.data, live=True)

        db.session.add(product)
        db.session.commit()
        form.image.data.save(img_path)

        return if_url_is_safe_redirect(url_for('admin_app.admin'), route_func_name_to_redirect_to='admin_app.add')
    return render_template('admin/add-product.html', admin=True, form=form)


@admin_app.route("/<int:page_number>")
@admin_app.route('/')
def admin(page_number=1):

    products = Product.query.filter(Product.live==True).paginate(per_page=_PER_PAGE, page=page_number, error_out=False)
    available_stocks = Product.query.filter(Product.stock > 0).count()
    pending_orders = User.query.filter(User.payment_status == "PENDING").count()
    completed_orders = User.query.filter(User.payment_status =="Complete").count()
    out_of_stock = abs(products.total - available_stocks)
    users = User.query.order_by(desc(User.id)).paginate(per_page=_PER_PAGE, page=page_number, error_out=False)

    return render_template('admin/home.html', admin=True, products=products, out_of_stock=out_of_stock,
                           available_stocks=available_stocks, users=users, page_number=page_number,
                           pending_orders=pending_orders, completed_orders=completed_orders)


@admin_app.route("/delete/<int:page_number>")
@admin_app.route("/delete/<int:product_id>")
def delete_item(product_id, page_number=1):

    product = Product.query.get(product_id)
    product.live = False
    db.session.add(product)
    db.session.commit()

    flash("The item has been remove from the database")

    if not is_safe_url(url_for("home_app.home", page_number=page_number)):
        abort(404)
    return redirect(url_for("home_app.home", page_number=page_number))


@admin_app.route("/complete/<order_id>/<page_number>")
def complete_order(order_id, page_number):

    order = Order.query.filter_by(id=order_id).first()

    if order.user.payment_status != "Complete":
        order.user.payment_status = "Complete"

        db.session.add(order)
        db.session.commit()
    return redirect(url_for("admin_app.admin", page_number=page_number))


@admin_app.route('/product/<int:user_id>')
def view_order(user_id):

    user = User.query.filter_by(id=user_id).first_or_404()
    return render_template('admin/view-product.html', admin=True, user=user, user_id=user_id)


@admin_app.route("/logout")
def admin_logout():

    if session.get("admin"):
        del session["admin"]
    return redirect(url_for("home_app.home"))