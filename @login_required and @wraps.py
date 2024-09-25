# from flask import Flask, render_template, redirect, url_for, request
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
#
# app = Flask(__name__)
# app.secret_key = 'secret-key'
#
# # Initialize Flask-Login
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
#
# # Dummy User Database
# users = {'dhanush': {'password': 'dhanush3003'}}
#
# # User Class
# class User(UserMixin):
#     def __init__(self, username):
#         self.id = username
#
# # User Loader
# @login_manager.user_loader
# def load_user(username):
#     if username in users:
#         return User(username)
#     return None
#
# # Login Route
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username in users and users[username]['password'] == password:
#             user = User(username)
#             login_user(user)
#             return redirect(url_for('protected'))
#         return 'Invalid credentials'
#     return '''
#     <form method="POST">
#         <input type="text" name="username" placeholder="Username">
#         <input type="password" name="password" placeholder="Password">
#         <button type="submit">Login</button>
#     </form>
#     '''
#
# # Protected Route
# @app.route('/protected')
# @login_required
# def protected():
#     print(current_user.id)
#     return f'Hello, {current_user.id}! You are logged in.'
#
# # Logout Route
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))
#
# # Home Route
# @app.route('/')
# def home():
#     return 'Welcome to the Home Page. <a href="/login">Login here</a>'
#
# if __name__ == '__main__':
#     app.run(debug=True)


# // ---------------------------------------------------------------------------------------

# def a_decorator(func):
#     def wrapper(*args , **kwargs):
#         # Extend some capabilities of func
#         func()
#
#     return wrapper
#
#
# @a_decorator
# def first_function():
#     print("first function")
#
#
# @a_decorator
# def second_function(a):
#     print("second function")
#
#
# print(first_function.__name__)
# # print(first_function.__doc__)
# # print(second_function.__name__)
# # print(second_function.__doc__)
