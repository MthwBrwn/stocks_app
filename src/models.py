from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from flask_migrate import Migrate
from . import app
# from passlib.hash import sha256_crypt


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.ForeignKey('portfolios.id'), nullable=False)
    symbol = db.Column(db.String(64), index=True, unique=True)
    companyName = db.Column(db.String(256), index=True, unique=True)
    exchange = db.Column(db.String(128))
    industry = db.Column(db.String(128))
    website = db.Column(db.String(128))
    description = db.Column(db.Text)
    CEO = db.Column(db.String(128))
    issueType = db.Column(db.String(128))
    sector = db.Column(db.String(128))

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<{}  {}>'.format(self. symbol, self.companyName)


class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True)
    # symbol = db.Column(db.String(64), index=True, unique=True)
    # companyName = db.Column(db.String(256), index=True, unique=True)
    # exchange = db.Column(db.String(128))
    # industry = db.Column(db.String(128))
    # website = db.Column(db.String(128))
    # description = db.Column(db.Text)
    # CEO = db.Column(db.String(128))
    # issueType = db.Column(db.String(128))
    # sector = db.Column(db.String(128))

    companies = db.relationship('Company', backref='portfolio', lazy=True)

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '< Portfolio : {} >'.format(self. name)
    # do things
    # def __init__(self, email, password):
    #     self.email = email
    #     self.password = sha256_crypt.encrypt(password)

# @classmethod
# def check_password_hash(cls, user password):
#     """
#     """
#     if sha256_ rypt.verify(password, user.password):
