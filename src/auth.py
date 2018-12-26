from flask import abort, render_template, flash, redirect, url_for, session, g
from .forms import AuthForm
from .models import User, db
from . import app
import functools


def login_required(view):
    """
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            abort(404)

        return view(**kwargs)

    return wrapped_view


@app.before_request
def load_logged_in_user():
    """This method is implicitly run before any other request to see if a user_id is available
    """
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Register handles routing to the register html and posting new registration data
    """
    form = AuthForm()

    if form.validate_on_submit():
        email = form.data['email']
        password = form.data['password']
        error = None

        if not email or not password:
            error = 'Invalid email or password'
        if User.query.filter_by(email=email).first() is not None:
            error = f'{email} has already been registered. '

        if error is None:
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()

            flash('Registration complete. Please log in ')
            return redirect(url_for('.login'))
        flash(error)

    return render_template('auth/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ login handles checking th login logic of the login html page
    """
    form = AuthForm()

    if form.validate_on_submit():
        email = form.data['email']
        password = form.data['password']
        error = None

        user = User.query.filter_by(email=email).first()

        if user is None or not User.check_password_hash(user, password):
            error = 'Invalid username or password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('portfolio_detail'))

        flash(error)
    return render_template('auth/login.html', form=form)


@app.route('/logout')
def logout():
    """ This handles the logic for a user logging out and clears session data
    """
    session.clear()
    flash('You are now logged out.')
    return redirect(url_for('.login'))
