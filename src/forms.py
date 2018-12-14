
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CompanySearchForm(FlaskForm):
    """This form sets up the ablity for the user to enter the symbol for
    a stock
    """

    symbol = StringField('symbol', validators=[DataRequired()])


class CompanyAddForm(FlaskForm):
    """
    """
    symbol = StringField('symbol', validators=[DataRequired("add to portfolio")])


# ####new work
# class AuthForm(FlaskForm):
# """
# """
# email   #finish here
