from flask import session, url_for, render_template, flash, request, Blueprint

from cart.form import UpdateCartForm, AddItemToCartForm
from user.models import Product
from utils.is_url_safe import if_url_is_safe_redirect
from utils.process_shipping_fee import process_shipping_fee


cart_app = Blueprint('cart_app', __name__, url_prefix="/cart")


@cart_app.route("product/quick/add/<int:product_id>")
def add_one_item_to_cart(product_id):

    _add_to_cart_helper(product_id, quantity=1)
    flash("An item has been added to your shopping cart")

    return if_url_is_safe_redirect(request.referrer, url_to_redirect_to=request.referrer)


@cart_app.route("/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):

    form = AddItemToCartForm()

    if form.validate_on_submit():

        if Product.query.filter_by(id=product_id).first().stock:
            _add_to_cart_helper(product_id, form.quantity.data)

    return if_url_is_safe_redirect(url_for('home_app.home'), route_func_name_to_redirect_to='home_app.home')


def _update_session_with_num_of_items_in_cart(item_num):

    if "cart" in session and "num_of_items" in session:
        session["num_of_items"] += item_num
    else:
        session["num_of_items"] = item_num
    session.modified = True


def _add_to_cart_helper(product_id, quantity, update=False):
    """_add_to_cart_helper(str, int, boolean) -> return None

      The add_to_cart_helper provides additional functionality to
      cart by adding items to the cart. The helper first checks if
      the item already exists in the cart. If it does it increments or decrements the
      quantity of items by the amount the user has chosen.

      If the item does not exists then it adds a item with a single quantity to cart.
      If the update "parameter" is set to true it allows the user to decrement the amount
      of items in the cart

      :parameter
        :product_id: The product id for the item
        :quantity: The number of items for the items.
        :update: Allows the user update the amount in their cart

    """

    if "cart" not in session:
        session["cart"] = {product_id: {"id": product_id, "quantity": quantity}}
    elif "cart" in session and not update and session["cart"].get(str(product_id)):
        session["cart"][str(product_id)]["quantity"] += quantity
    elif "cart" in session and update and session["cart"].get(str(product_id)):
       _update_cart_quantity(product_id, new_quantity=quantity)
    else:
        session["cart"].update({str(product_id): {"id": product_id, "quantity": quantity}})

    if not update:
        _update_session_with_num_of_items_in_cart(quantity)
    session.modified = True


def _update_cart_quantity(product_id, new_quantity):

    current_quantity = session["cart"][str(product_id)]["quantity"]
    difference = abs(current_quantity - new_quantity)

    if current_quantity > new_quantity:

        session["num_of_items"] -= difference
    else:
        session["num_of_items"] += difference

    session["cart"][str(product_id)]["quantity"] = new_quantity
    session.modified = True


@cart_app.route("/remove/item/<product_id>")
def remove_item_from_cart(product_id):

    session["num_of_items"] -= session["cart"][str(product_id)]["quantity"]

    del session["cart"][str(product_id)]

    session.modified = True

    return if_url_is_safe_redirect(url_for('cart_app.cart'), route_func_name_to_redirect_to='cart_app.cart')


@cart_app.route('/')
def cart():

    grand_total = 0
    products = []
    form = UpdateCartForm()
    num_of_items_in_cart = 0

    for product_id in session.get("cart", ""):
        product = Product.query.filter_by(id=int(product_id)).first()
        quantity = session["cart"][str(product_id)]['quantity']
        product.live = True
        total = quantity * product.price
        num_of_items_in_cart += quantity
        grand_total += total

        items = {"name": product.name, "price": product.price, "image": product.image, "quantity": quantity,
                         "total": round(total, 2), "id": product.id, "stock": product.stock}

        if items not in products:
            products.append(items)

    session["grand_total"] = grand_total
    session["products"] = products
    session.modified = True
    shipping_cost, shipping_fee = process_shipping_fee(grand_total)

    return render_template('cart/cart.html', cart_items=products, grand_total=round(grand_total, 2),
                           shipping_costs=shipping_cost, shipping_fee=shipping_fee, total_items=len(products), form=form)


@cart_app.route("/update/cart-quantity/<int:product_id>/", methods=["POST"])
def update_cart(product_id):

    form = UpdateCartForm()

    if form.validate_on_submit():
        _add_to_cart_helper(product_id, form.quantity.data, update=True)

    return if_url_is_safe_redirect(url_for('cart'), route_func_name_to_redirect_to='cart')
