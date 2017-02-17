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
    except FlowExchangeError as e:
        print(str(e))
        return False

    os.chdir(os.path.dirname(os.path.realpath(__file__)).replace('/oauth', '') + '/oauth/credentials')

    file_name = '{id}.json'.format(id=usr.id)
    open(file_name, 'a').close()
    storage = Storage(file_name)
    storage.put(credentials)
    return True
