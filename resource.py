import requests
from app import app


def rand_user(count):
    result = requests.get(f'https://randomuser.me/api/?results={count}&inc=name,email,picture&noinfo')
    return result.json()


@app.route('/randusers/<int:count>', methods=['GET'])
def get_users(count):
    return rand_user(count), 200

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome</h1> <br> Visit <code>https://uni-challenge-randuser.herokuapp.com/randusers/(count) </code> to receive random user data of the specified count. Example for 5 users: https://uni-challenge-randuser.herokuapp.com/randusers/5"
