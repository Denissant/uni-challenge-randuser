from app import app
from modules import rand_user, create_html_string, html_string


@app.route('/users_raw/<int:count>', methods=['GET'])
def get_users(count):
    return rand_user(count), 200


@app.route('/users/<int:count>', methods=['GET'])
def get_users_pretty(count):
    received_data = rand_user(count)['results']
    return create_html_string(received_data, html_string), 200


@app.route('/', methods=['GET'])
def home():
    return """<h1>Welcome</h1> <br> Visit <code>https://uni-challenge-randuser.herokuapp.com/users/(count)</code>\
    to receive random user data of the specified count.\
    <br><br> Example for 100 users: <a href=https://uni-challenge-randuser.herokuapp.com/users/100>https://uni-challenge-randuser.herokuapp.com/users/100</a>\
    <br><br> You can also generate raw JSON data (example for 10 users: <a href=https://uni-challenge-randuser.herokuapp.com/users_raw/10>https://uni-challenge-randuser.herokuapp.com/users_raw/10</a>)
    <br><br> Maximum count: 5000"""
