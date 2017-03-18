from flask import render_template, Flask, request
import requests
import json
import os

LOCALHOST = "http://localhost:5000" #os.environ['LOCALHOST']

app = Flask(__name__)


@app.route('/index/<user_id>')
def index(user_id):
    count = request.args.get('count')
    if not count:
        count = 10
    else:
        count = int(count)

    # posts_request = requests.get('http://188.166.174.189:28104/sort/%s?count=%s' % (user_id, count))
    posts_request = requests.get('http://localhost:5001/sort/%s?count=%s' % (user_id, count))

    # posts_request = requests.get('http://pocket-square-sort-shuffle:5000/sort/' + user_id)
    posts = posts_request.json()

    for post in posts:
        post['similar_url'] = '%s/index/%s/similar/%s' % (LOCALHOST, user_id, post['id'])

    user_request = requests.get('http://188.166.174.189:28101/user/' + user_id)
    user = user_request.json()

    return render_template('index.html', posts=posts, user=user, load_more_url='%s/index/%s?count=%s' % (LOCALHOST, user_id, str(count + 10)))


@app.route('/index/<user_id>/similar/<text_id>')
def similar(user_id, text_id):
    # posts_request = requests.get('http://pocket-square-similar-by-text:5000/%s/%s/similar_by_text' % (user_id, text_id))
    posts_request = requests.get('http://188.166.174.189:28105/%s/%s/similar_by_text' % (user_id, text_id))
    posts = posts_request.json()

    return render_template('similar.html', posts=posts[1:], original_post=posts[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
