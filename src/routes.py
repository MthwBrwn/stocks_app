from . import app

from flask import render_template, abort, redirect, url_for, request, flash, session
from .forms import CompanySearchForm, CompanyAddForm, PortfolioCreateForm
from sqlalchemy.exc import DBAPIError, IntegrityError
from .models import db, Company, Portfolio
from json import JSONDecodeError
import requests as req
import json
# from .auth import
import os


@app.add_template_global
def get_portfolios():
    """This decorator makes it so that the companies who are required to have a portfolio
    can locate a portfolio
    """
    return Portfolio.query.all()


@app.route('/')
def home():
    """ This is the home page of the stocks app
    """
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def company_search():
    """In this route the user is taken to the search page where a selection can be made for a company.
    """
    form = CompanySearchForm()

    if form.validate_on_submit():
        symbol = form.data['symbol']
        res = req.get(f'https://api.iextrading.com/1.0/stock/{ form.data["symbol"] }/company')
        data = json.loads(res.text)
        session['context'] = data
        session['symbol'] = symbol
        # import pdb; pdb.set_trace()
        # session['portfolio_id'] = form.data['portfolios']

        return redirect(url_for('.portfolio_preview'))
        # except JSONDecodeError:
        #     flash('The company could not be found.')

    return render_template('portfolio/search.html', form=form)


@app.route('/company', methods=['GET', 'POST'])
def portfolio_preview():
    """ This route shows the detail fo the company after the company is selected by User
    """
    try:
        form_context = {
            'symbol': session['symbol'],
            'companyName': session['context']['companyName'],
        }
        # import pdb; pdb.set_trace()
        # session['symbol'] = symbol
        form = CompanyAddForm(**form_context)
        if form.validate_on_submit():
            try:
                form_data = {
                    'symbol': form.data['symbol'],
                    'companyName': form.data['companyName'],
                    'exchange': form.data['exchange'],
                    'industry': form.data['industry'],
                    'website': form.data['website'],
                    'description': form.data['description'],
                    'CEO': form.data['CEO'],
                    'issueType': form.data['issueType'],
                    'sector': form.data['sector'],
                    'portfolio_id': form.data['portfolios']
                }
                company = Company(**form_data)
                db.session.add(company)
                # import pdb; pdb.set_trace()
                db.session.commit()

            except (IntegrityError, DBAPIError):

                flash("You can only add a company to your portfolio once.")
                return render_template('portfolio/search.html', form=form)

            return redirect(url_for('.company_search'))

        return render_template(
            'portfolio/company.html',
            form=form,
            symbol=form_context['symbol']
            # context_data=session['context']
        )
    except JSONDecodeError:
        flash('That company cannot be located')
        return redirect(url_for('.company_search'))


@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio_detail():
    """ This routes to the page where the portfolios of company data is shown
    """
    form = PortfolioCreateForm()

    if form.validate_on_submit():
        try:
                portfolio = Portfolio(name=form.data['name'])
                db.session.add(portfolio)
                db.session.commit()

        except (IntegrityError, DBAPIError):

            flash("Something is wrong with your portfolio. Please try again")
            return render_template('portfolio/portfolio.html', form=form)

        return redirect(url_for('.company_search'))

    companies = Company.query.all()
    return render_template('portfolio/portfolio.html', companies=companies, form=form)
