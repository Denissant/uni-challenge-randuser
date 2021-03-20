import requests
from app import app
from flask import make_response


def rand_user(count):
    result = requests.get(f'https://randomuser.me/api/?results={count}&inc=name,email,picture&noinfo')
    return result.json()


@app.route('/randusers/<int:count>', methods=['GET'])
def get_users(count):
    resp = make_response(rand_user(count))
    resp.headers['Content-Encoding'] = 'unicode, utf8, utf-8'
    resp.headers['Accept-Encoding'] = 'utf-8'
    return resp, 200


@app.route('/', methods=['GET'])
def home():
    return """<h1>Welcome</h1> <br> Visit <code>https://uni-challenge-randuser.herokuapp.com/randusers/(count) </code>\
    to receive random user data of the specified count.\
    <br><br> Example for 5 users: <a href=https://uni-challenge-randuser.herokuapp.com/randusers/5>https://uni-challenge-randuser.herokuapp.com/randusers/5</a>"""
