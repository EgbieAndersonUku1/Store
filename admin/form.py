from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField


class AdminLoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired(), validators.Length(min=5, max=5)])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=3, max=255)])
