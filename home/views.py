from flask import render_template, Blueprint

from user.models import Product

home_app = Blueprint('home_app', __name__)


@home_app.route('/<int:page_number>')
@home_app.route('/')
def home(page_number=1):

    PER_PAGE = 10
    products = Product.query.filter(Product.live==True).paginate(per_page=PER_PAGE, page=page_number, error_out=True)

    return render_template('/home/home.html', products=products, page_number=page_number)
