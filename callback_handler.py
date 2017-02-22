import sqlite3
from datetime import datetime, timedelta
import random
import string

from flask import Flask, redirect
from flask import request
app = Flask(__name__)

conn = sqlite3.connect('users.db')
c = conn.cursor()


@app.route('/google_oauth')
def google_oauth():
    code = str(request.args['code'])
    short_code = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    c.execute('INSERT INTO cache_oauth_codes VALUES(?, ?, ?)', (code, short_code, datetime.now()))
    c.execute('DELETE FROM cache_oauth_codes WHERE created_at < ?', (datetime.now() - timedelta(days=1)))
    conn.commit()

    return redirect('https://telegram.me/CompleteGoogleBot?start=oauth-' + code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=4999)
