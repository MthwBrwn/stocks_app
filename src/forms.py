
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from .models import Portfolio


class CompanySearchForm(FlaskForm):
    """This form sets up the ability for the user to enter the symbol for
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
    portfolios = SelectField('portfolios')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolios.choices = [(str(p.id), p.name) for p in Portfolio.query.all()]


class PortfolioCreateForm(FlaskForm):
    """This class creates a new portfolio in which the collection of companies are kept
    """
    name = StringField('name', validators=[DataRequired()])
