from app import app
from resources import home, get_users, get_users_pretty

if __name__ == '__main__':
    app.run(port=5040, debug=True)
