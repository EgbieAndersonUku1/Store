from flask import Blueprint, render_template

from product.forms import AddProductToCartForm
from product.type import ITEM_TYPES
from user.models import Product

product_app = Blueprint('product_app', __name__, url_prefix="/product")

_PER_PAGE = 16


@product_app.route('/<int:product_id>', methods=["GET", "POST"])
def product(product_id):

    product = Product.query.get_or_404(product_id)
    return render_template('products/view-product.html', product=product, form=AddProductToCartForm())


@product_app.route("/trousers/<int:page_number>")
@product_app.route("/trousers")
def get_trousers(page_number=1):

    trousers = Product.query.filter(Product.type == ITEM_TYPES["TROUSERS"], Product.live==True).paginate(per_page=_PER_PAGE,
                                                                                                         page=page_number,
                                                                                                         error_out=False)
    return render_template("products/trousers.html", trousers=trousers, page_number=page_number)


@product_app.route("/tops/<int:page_number>")
@product_app.route("/tops")
def get_tops(page_number=1):

    tops = Product.query.filter(Product.type == ITEM_TYPES["TOPS"], Product.live==True).paginate(per_page=_PER_PAGE,
                                                                                                 page=page_number,
                                                                                                 error_out=False)
    return render_template("products/tops.html", tops=tops, page_number=page_number)


@product_app.route("/sports/wear/<page_number>")
@product_app.route("/sports/wear")
def get_sports_wear(page_number=1):

    sports_wear = Product.query.filter(Product.type == ITEM_TYPES["SPORTS_WEAR"], Product.live==True).paginate(per_page=_PER_PAGE,
                                                                                                               page=page_number,
                                                                                                               error_out=False)
    return render_template("/products/sports_wear.html", sports_wear=sports_wear, page_number=page_number)


@product_app.route("/lingerie/<int:page_number>")
@product_app.route("/lingerie")
def get_lingerie(page_number=1):

    lingeries = Product.query.filter(Product.type == ITEM_TYPES["LINGERIE"], Product.live==True).paginate(per_page=_PER_PAGE,
                                                                                                          page=page_number,
                                                                                                          error_out=False)
    return render_template("products/lingerie.html", lingeries=lingeries, page_number=page_number)


@product_app.route("/shoes/<int:page_number>")
@product_app.route("/shoes")
def get_shoes(page_number=1):
    shoes = Product.query.filter(Product.type == ITEM_TYPES["SHOES"], Product.live==True).paginate(per_page=_PER_PAGE,
                                                                                                   page=page_number, error_out=False)
    return render_template("products/shoes.html", shoes=shoes, page_number=page_number)


@product_app.route("/hoodies/<int:page_number>")
@product_app.route("/hoodies")
def get_hoodies(page_number=1):
    hoodies = Product.query.filter(Product.type == ITEM_TYPES["HOODIES"], Product.live==True).paginate(per_page=_PER_PAGE,
                                                                                                       page=page_number, error_out=False)
    return render_template("products/hoodies.html", hoodies=hoodies, page_number=page_number)


@product_app.route("/hats/<int:page_number>")
@product_app.route("/hats")
def get_hats(page_number=1):
    hats = Product.query.filter(Product.type == ITEM_TYPES["HATS"], Product.live==True).paginate(per_page=_PER_PAGE,
                                                                                                 page=page_number, error_out=False)
    return render_template("products/hats.html", hats=hats, page_number=page_number)

