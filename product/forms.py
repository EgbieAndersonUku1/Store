from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, FloatField, IntegerField, SelectField, FileField, HiddenField, validators
from wtforms.widgets import TextArea

from product.type import TYPES


class ProductForm(FlaskForm):
    """The flask form that would be displayed to the user at the frontend"""
    name = StringField('Product name', validators=[validators.DataRequired(), validators.Length(3, 50)])
    price = FloatField('Price', validators=[validators.DataRequired()])
    stock = IntegerField('Stock', validators=[validators.DataRequired()])
    description = StringField('Description', widget=TextArea(), validators=[validators.DataRequired(),
                                                                            validators.Length(min=51)])
    type = SelectField("Item type", choices=TYPES)

    image = FileField("Image", validators=[FileRequired(), FileAllowed(["jpg", "jpeg", "png", "gif"],
                    "Only files with the following extensions .jpg, .jpeg, .png, .gif are allowed")
    ])


class AddProductToCartForm(FlaskForm):
    """A form that is used at the frontend which enables the user to add the number of items to a cart."""
    quantity = IntegerField("Quantity", validators=[validators.DataRequired()])
    id = HiddenField("ID")
