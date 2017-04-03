# Copyright (c) 2017 Marco Aceti <dev@marcoaceti.it>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from config import *

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
    if request.args.get('error'):
        return '<h1>Fatal error</h1>\n<a href="https://telegram.me/{u}">Retry</a>'.format(u=BOT_USERNAME)

    code = str(request.args.get('code'))
    short_code = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    c.execute('INSERT INTO cache_oauth_codes VALUES(?, ?, ?)', (code, short_code, datetime.now()))
    conn.commit()

    return redirect('https://telegram.me/{u}?start=oauth-{sc}'.format(u=BOT_USERNAME, sc=short_code))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=4999)
