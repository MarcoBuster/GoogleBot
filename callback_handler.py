import sqlite3
from datetime import datetime
import random
import string

from flask import Flask, redirect
from flask import request
app = Flask(__name__)

conn = sqlite3.connect('users.sqlite')
c = conn.cursor()


@app.route('/google_oauth')
def google_oauth():
    code = str(request.args['code'])
    short_code = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    c.execute('INSERT INTO cache_oauth_codes VALUES(?, ?, ?)', (code, short_code, datetime.now()))
    conn.commit()

    return redirect('https://telegram.me/CompleteGoogleBot?start=oauth-' + short_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=4999)
