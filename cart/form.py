from flask_wtf import FlaskForm
from wtforms import IntegerField, HiddenField, validators


class UpdateCartForm(FlaskForm):
    """A form that is used at the frontend which enables the user to add the number of items to a cart."""
    quantity = IntegerField("Quantity", validators=[validators.DataRequired()])
    id = HiddenField("ID")


class AddItemToCartForm(FlaskForm):
    """A form that is used at the frontend which enables the user to add the number of items to a cart."""
    quantity = IntegerField("Quantity", validators=[validators.DataRequired()])
    id = HiddenField("ID")