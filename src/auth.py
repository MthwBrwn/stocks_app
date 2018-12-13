from . import app

@app.route('/register', method=['GET', 'POST'])
def login():
    """
    """
    pass

@app.route('logout')
def logout():
    """
    """

#finish this
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    """
    form = AuthForm()

    if form.validate_on_submit():
        email = form.data['email']
        password = form.data['password']
        error = None

        user =User.query.filter_by(email=email).first
