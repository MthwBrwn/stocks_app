from . import app

from flask import render_template, abort, redirect, url_for, request, flash, session
from sqlalchemy.exc import DBAPIError, IntegrityError
from json import JSONDecodeError
from .models import db, Company
from .forms import CompanySearchForm, CompanyAddForm
import requests as req
import json
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


@app.route('/preview')
def portfolio_preview():
    """ This route shows the detail fo the company after the company is selected by User
    """
    form_context = session['context']
    # import pdb; pdb.set_trace()
    form = CompanyAddForm(**form_context)
    # try:
    #     data = json.loads(res.text)
    #     company = Company(
    #         symbol=data['symbol'],
    #         companyName=data['companyName'],
    #         exchange=data['exchange'],
    #         industry=data['industry'],
    #         website=data['website'],
    #         description=data['description'],
    #         CEO=data['CEO'],
    #         issueType=data['issueType'],
    #         sector=data['sector'],
        # )

        #     # NOTE: THIS WILL THROW A DUPE KEY ERROR IF WE ADD THE SAME STOCK AGAIN
        #     # Handle this with an additional try/except
        #     db.session.add(company)
        #     db.session.commit()

        # except (DBAPIError, IntegrityError):
        #     flash("You can only add a company to your portfolio once.")
        #     return render_template('portfolio/search.html', form=form)

    return render_template('portfolio/preview.html', form=form)


@app.route('/portfolio')
def portfolio_detail():
    """
    """
    return render_template('portfolio/portfolio.html')
