from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "привет"
@app.route('/hello')
def hello_world():
    return "Hello World!"
@app.route('/user/<username>')
def user(username):
    return f"page of {username}"
app.run(debug=True)
