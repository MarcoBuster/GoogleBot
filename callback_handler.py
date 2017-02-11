from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/google_oauth')
def test():
    code = str(request.args['code'])
    url = 'https://telegram.me/CompleteGoogleBot?start=oauth@'+code
    return '<big><big><b><a href="{url}">Click here</a></b></big></big>'.format(url=url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=4999)
