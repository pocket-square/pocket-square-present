from flask import render_template, Flask, request
import requests
import os
import yaml
import time

with open("application.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

if os.environ.has_key('SERVICE_ENVIRONMENT'):
    environment = os.environ['SERVICE_ENVIRONMENT']
else:
    environment = cfg['default_environment']

app = Flask(__name__)


@app.route('/index/<user_id>')
def index(user_id):
    count = request.args.get('count')
    if not count:
        count = 10
    else:
        count = int(count)

    posts_request = requests.get('%s/sort/%s?count=%s' % (cfg[environment]['pocket_square_sort_service'], user_id, count))
    posts = posts_request.json()

    for post in posts:
        post['similar_url'] = '%s/index/%s/similar/%s' % (cfg[environment]['host'], user_id, post['id'])
        post['timeAdded'] = time.ctime(post['timeAdded'])

    user_request = requests.get('%s/user/%s' % (cfg[environment]['pocket_square_user_service'], user_id))
    user = user_request.json()

    return render_template('index.html', posts=posts, user=user, load_more_url='%s/index/%s?count=%s' % (cfg[environment]['host'], user_id, str(count + 10)))


@app.route('/index/<user_id>/similar/<text_id>')
def similar(user_id, text_id):
    posts_request = requests.get('%s/%s/%s/similar_by_text' % (cfg[environment]['pocket_square_similar_by_text_service'], user_id, text_id))
    posts = posts_request.json()

    return render_template('similar.html', posts=posts[1:], original_post=posts[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=cfg[environment]['port'], debug=cfg[environment]['debug'])
