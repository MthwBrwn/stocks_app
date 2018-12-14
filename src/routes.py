from . import app

from flask import render_template, abort, redirect, url_for, request, flash, session
from sqlalchemy.exc import DBAPIError, IntegrityError
from json import JSONDecodeError
from .models import db, Company
from .forms import CompanySearchForm, CompanyAddForm
import requests as req
import json
# from .auth import
import os


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
        # symbol = form.data['symbol']
        # res = req.get(f'https://api.iextrading.com/1.0/stock/{ request.form("symbol")}/company')
        res = req.get(f'https://api.iextrading.com/1.0/stock/{ form.data["symbol"] }/company')
        data = json.loads(res.text)
        try:
            session['context'] = data

            return redirect(url_for('.portfolio_preview'))
        except JSONDecodeError:
            flash('The company could not be found.')
    return render_template('portfolio/search.html', form=form)


@app.route('/preview', methods=['GET', 'POST'])
def portfolio_preview():
    """ This route shows the detail fo the company after the company is selected by User
    """
    try:
        form_context = session['context']
        form = CompanyAddForm(**form_context)
        if form.validate_on_submit():
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
            }
            try:
                company = Company(**form_data)
                # import pdb; pdb.set_trace()
                db.session.add(company)

                db.session.commit()

            except (DBAPIError, IntegrityError):
                flash("You can only add a company to your portfolio once.")
                return render_template('portfolio/search.html', form=form)

            return redirect(url_for('.company_search'))

        return render_template('portfolio/preview.html', form=form)

    except JSONDecodeError:
        flash ('That company cannot be located')
        return redirect(url_for('.company_search'))

@app.route('/portfolio')
def portfolio_detail():
    """ This routes to the page where the company data is shown
    """
    companies = Company.query.all()
    return render_template('portfolio/portfolio.html', companies=companies)
