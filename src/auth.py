# from . import app


# def login_required(view):
#     """
#     """
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             abort(404)
#             #return redirect(url_for(.)





# @app.route('/register', method = ['GET', 'POST'])
# def login():
#     """
#     """
#     pass

# @app.route('logout')
# def logout():
#     """
#     """

# #finish this
# @app.route('/login', method = ['GET', 'POST'])
# def login():
#     """
#     """
#     form = AuthForm()

#     if form.validate_on_submit():
#         email = form.data['email']
#         password = form.data['password']
#         error = None

#         user =User.query.filter_by(email=email).first
