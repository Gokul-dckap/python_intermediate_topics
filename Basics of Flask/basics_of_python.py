# pip install Flask

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user')
def hello_world():
    return 'Hello, World!'

@app.route('/user')
def hello_world():
    return f'Hello,!'

@app.route('/welcome/<name>')
def welcome_user(name):
    return render_template('welcome.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
