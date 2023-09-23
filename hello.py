from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#Example 2-2
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)