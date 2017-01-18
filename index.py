from flask import render_template, Flask
from urllib2 import Request, urlopen, URLError
import json

app = Flask(__name__)


@app.route('/index')
def index():
    request = Request('http://localhost:5001/sort')
    try:
        response_json = urlopen(request).read()
        response = json.loads(response_json)
        return render_template('index.html', posts=response)
    except URLError, e:
        return 'Something went wrong:', e


if __name__ == '__main__':
    app.run(debug=True)
