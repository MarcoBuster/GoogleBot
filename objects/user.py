# Copyright (c) 2017 The TelegramGoogleBot Authors (see AUTHORS)
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


import sqlite3
from languages import it, en, es
import os
from oauth2client.file import Storage

conn = sqlite3.connect('users.sqlite')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users'
          '(id INTEGER PRIMARY KEY NOT NULL, state TEXT, language TEXT, timezone TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS calendar_create_event'
          '(id INTEGER NOT NULL, summary TEXT, description TEXT)')  # Only for caching messages
c.execute('CREATE TABLE IF NOT EXISTS calendar_update_event'
          '(id INTEGER NOT NULL, event TEXT, summary TEXT, description TEXT)')  # Only for caching messages
c.execute('CREATE TABLE IF NOT EXISTS cache_oauth_codes(code TEXT, short_code TEXT, created_at DATETIME)')
c.execute('CREATE TABLE IF NOT EXISTS cache_calendar_page_tokens(token TEXT, short_token TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS cache_calendar_event_ids(id TEXT, short_id TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS cache_drive_page_tokens(token TEXT, short_token TEXT)')
conn.commit()


class User:
    conn = sqlite3.connect('users.sqlite')
    c = conn.cursor()

    def __init__(self, user, language=None, state=None):
        self.id = user.id
        self.name = user.name
        self.username = user.username
        if language is not None:
            c.execute('UPDATE OR IGNORE users SET language=? WHERE id=?', (language, self.id,))
            conn.commit()
            return

        if state is not None:
            c.execute('UPDATE OR IGNORE users SET state=? WHERE id=?', (state, self.id,))
            conn.commit()
            return

        c.execute('INSERT OR IGNORE INTO users VALUES(?, ?, ?, ?)', (self.id, state, language, None))
        conn.commit()

    @property
    def exists(self):
        c.execute('SELECT language FROM users WHERE id=?', (self.id,))
        row = c.fetchone()
        if not row or row[0] is None:
            return False
        return True

    def language(self, new_language=None):
        if new_language is None:
            c.execute('SELECT language FROM users WHERE id=?', (self.id,))
            row = c.fetchone()
            if not row:
                return False
            return row[0]

        c.execute('UPDATE OR IGNORE users SET language=? WHERE id=?', (new_language, self.id))
        conn.commit()

    def timezone(self, new_timezone=None):
        if new_timezone is None:
            c.execute('SELECT timezone FROM users WHERE id=?', (self.id,))
            row = c.fetchone()
            if not row or row[0] is None:
                return False
            return row[0]

        c.execute('UPDATE OR IGNORE users SET timezone=? WHERE id=?', (new_timezone, self.id))
        conn.commit()

    def state(self, new_state=None):
        if new_state is None:
            c.execute('SELECT state FROM users WHERE id=?', (self.id,))
            row = c.fetchone()
            if not row:
                return False
            else:
                return row[0]
        else:
            c.execute('UPDATE OR IGNORE users SET state=? WHERE id=?', (new_state, self.id,))
            conn.commit()

    def getstr(self, str_code):
        lang = self.language()
        if lang == 'it':
            return it.get(str_code)
        if lang == 'en':
            return en.get(str_code)
        if lang == 'es':
            return es.get(str_code)

    @property
    def logged_in(self):
        try:
            os.chdir(os.path.dirname(os.path.realpath(__file__)).replace('/objects', '') + '/oauth/credentials')

            storage = Storage('{id}.json'.format(id=self.id))
            if storage.get() is None:
                return False
            else:
                return True
        except:
            return False

    def credentials(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)).replace('/objects', '') + '/oauth/credentials')
        storage = Storage('{id}.json'.format(id=self.id))
        return storage.get()
