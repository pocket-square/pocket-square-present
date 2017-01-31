from flask import render_template, Flask
import requests
import json

app = Flask(__name__)


@app.route('/index/<user_id>')
def index(user_id):
    posts_request = requests.get('http://pocket_square_sort_shuffle:5000/sort/' + user_id)
    posts = posts_request.json()

    user_request = requests.get('http://pocket_square_users:8080/user/' + user_id)
    user = user_request.json()
    
    return render_template('index.html', posts=posts, user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
