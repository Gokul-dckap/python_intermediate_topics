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

# from flask import Flask, redirect, url_for, session, request, g
# from functools import wraps
#
# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Needed for session management
#
# # Sample user data for demonstration
# users = {
#     'user1': 'password1',
#     'user2': 'password2'
# }
#
# # Simulated login status
# def is_logged_in():
#     return 'username' in session
#
# # Login required decorator
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if not is_logged_in():
#             return redirect(url_for('login', next=request.url))
#         return f(*args, **kwargs)
#     return decorated_function
#
# @app.route('/')
# def home():
#     return "Welcome to the Home Page!"
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username in users and users[username] == password:
#             session['username'] = username
#             return redirect(url_for('protected'))
#         return "Invalid Credentials"
#     return '''
#         <form method="post">
#             Username: <input type="text" name="username"><br>
#             Password: <input type="password" name="password"><br>
#             <input type="submit" value="Login">
#         </form>
#     '''
#
# @app.route('/protected')
# @login_required
# def protected():
#     print(session)
#     return f"Hello, {session['username']}! This is a protected page."
#
# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('home'))
#
# if __name__ == '__main__':
#     app.run(debug=True)
