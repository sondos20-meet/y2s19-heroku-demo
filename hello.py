from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/hello')
def hello():
    return render_template(
        'hello.html', n = ‘something’)


if __name__ == '__main__':
    app.run(debug=True)