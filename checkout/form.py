from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators
from wtforms.fields.html5 import EmailField

from checkout.countries import CHOICES


class CheckOutForm(FlaskForm):
    title = SelectField('Title', choices=[("Mr", "Mr"), ("Mrs", "Mrs"), ("Miss", "Miss")])
    first_name = StringField("First Name", validators=[validators.DataRequired(), validators.Length(min=3, max=80)])
    surname = StringField("Surname", validators=[validators.DataRequired(), validators.Length(min=3, max=80)])
    address = StringField("Address", validators=[validators.DataRequired(), validators.Length(max=255)])
    city = StringField("City", validators=[validators.DataRequired(), validators.Length(min=3, max=80)])
    phone_number = StringField("Phone number UK format", validators=[validators.DataRequired(), validators.Length(max=13)])
    state = StringField("State", validators=[validators.DataRequired(), validators.Length(max=5)])
    email = EmailField("Email", validators=[validators.Email()])
    country = SelectField("Country", choices=CHOICES)
    payment_type = SelectField("Payment option", choices=[("PC", "Pay by Card"), ("BT", "Bank transfer")])

