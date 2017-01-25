from flask import render_template, Flask
from urllib2 import Request, urlopen, URLError
import json

app = Flask(__name__)


@app.route('/index/<user_id>')
def index(user_id):
    request = Request('http://pocket_square_sort_shuffle:28104/sort/' + user_id)
    try:
        response_json = urlopen(request).read()
        response = json.loads(response_json)
        return render_template('index.html', posts=response)
    except URLError, e:
        return 'Something went wrong:', e


if __name__ == '__main__':
    app.run(host='0.0.0.0')
