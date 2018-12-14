
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CompanySearchForm(FlaskForm):
    """This form sets up the ablity for the user to enter the symbol for
    a stock
    """

    symbol = StringField('symbol', validators=[DataRequired()])


class CompanyAddForm(FlaskForm):
    """This form creates the 2nd form in which the stock information selected by user is added.
    """
    symbol = StringField('symbol', validators=[DataRequired()])
    companyName = StringField('companyName', validators=[DataRequired()])
    exchange = StringField('exchange')
    industry = StringField('industry')
    website = StringField('website')
    description = StringField('description')
    CEO = StringField('CEO')
    issueType = StringField('issueType')
    sector = StringField('sector')


# ####new work
# class AuthForm(FlaskForm):
# """
# """
# email   #finish here
