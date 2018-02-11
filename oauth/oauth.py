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


from oauth2client.client import OAuth2WebServerFlow, FlowExchangeError
from oauth2client.file import Storage
import os
from config import *

SCOPES = ['https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/drive',
          'profile']

flow = OAuth2WebServerFlow(client_id=GOOGLE_OAUTH_CLIENT_ID,
                           client_secret=GOOGLE_OAUTH_CLIENT_SECRET,
                           scope=SCOPES,
                           redirect_uri=GOOGLE_OAUTH_REDIRECT_URI,
                           access_type='offline',
                           prompt='consent'
                           )


def get_url():
    return flow.step1_get_authorize_url()


def save(usr, code):
    try:
        credentials = flow.step2_exchange(code)
    except FlowExchangeError:
        return False

    os.chdir(os.path.dirname(os.path.realpath(__file__)).replace('/oauth', '') + '/oauth/credentials')

    file_name = '{id}.json'.format(id=usr.id)
    open(file_name, 'a').close()
    storage = Storage(file_name)
    storage.put(credentials)
    return True
