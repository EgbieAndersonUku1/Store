from secrets import token_hex

from flask import session, Blueprint, url_for, render_template, redirect, abort

from create_app import db
from checkout.form import CheckOutForm
from user.models import User, Order, Product
from utils.is_url_safe import is_safe_url
from utils.process_shipping_fee import _is_shipping_free

checkout_app = Blueprint("checkout_app", __name__, url_prefix="/checkout")

_SHIPPING_FEE = 50


@checkout_app.route('/', methods=["GET", "POST"])
def checkout():

    form = CheckOutForm()

    if form.validate_on_submit():
        reference_num = token_hex(15)
        user = User()
        form.populate_obj(obj=user)
        user.payment_status = "PENDING"
        user.reference_num = reference_num

        _add_all_bought_item_in_session_to_user_obj(user)

        if not is_safe_url(url_for('order_completion.app.order_completion', reference_number=reference_num)):
            abort(404)
        return redirect(url_for('order_completion_app.order_completion', reference_number=reference_num))

    return render_template('checkout/checkout.html', form=form, is_shipping_cost_free=_is_shipping_free)


def _add_all_bought_item_in_session_to_user_obj(user):

    for item in session["products"]:
        user_order = Order(quantity=item["quantity"], product_id=item["id"])
        user.items.append(user_order)
        Product.query.filter_by(id=item["id"]).update({'stock': Product.stock - item["quantity"]})

        if not _is_shipping_free(session.get("grand_total")):
            user_order.total_order = round(session["grand_total"] + _SHIPPING_FEE, 2)
        else:
            user_order.total_order = session["grand_total"]

    db.session.add(user)
    db.session.commit()
    _clear_cart_session()


def _clear_cart_session():
    """Clears all items that is related to the item's bought in the cart"""
    session.pop("cart")
    session.pop("grand_total")
    session.pop("products")
    session.pop("num_of_items")
    session.modified = True


