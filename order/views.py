from flask import render_template, Blueprint


order_completion_app = Blueprint("order_completion_app", __name__)


@order_completion_app.route("/order/completion/<reference_number>")
def order_completion(reference_number):
    return render_template("orders/order_completion.html", reference_num=reference_number)