from flask import render_template, Flask
import requests
import json

app = Flask(__name__)


@app.route('/index/<user_id>')
def index(user_id):
    posts_request = requests.get('http://pocket_square_sort_shuffle:5000/sort/' + user_id)
    posts = posts_request.json()

    for post in posts:
        post['similar_url'] = 'http://188.166.174.189:8080/index/%s/similar/%s' % (user_id, post['id'])

    user_request = requests.get('http://pocket_square_users:8080/user/' + user_id)
    user = user_request.json()

    return render_template('index.html', posts=posts, user=user)


@app.route('/index/<user_id>/similar/<text_id>')
def similar(user_id, text_id):
    posts_request = requests.get('http://pocket_square_similar_by_text:5000/%s/%s/similar_by_text' % (user_id, text_id))
    posts = posts_request.json()

    return render_template('similar.html', posts=posts[1:], original_post=posts[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
