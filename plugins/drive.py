from apiclient import discovery
import httplib2

import sqlite3

conn = sqlite3.connect('users.sqlite')
c = conn.cursor()


def login(user):
    credentials = user.credentials()
    http = credentials.authorize(httplib2.Http())
    return discovery.build('drive', 'v3', http=http)


def getfiles(user, elements_range):
    service = login(user)
    results = service.files().list(
        pageSize=elements_range[1], orderBy='modifiedByMeTime', pageToken=elements_range[0],
        q='not trashed and sharedWithMe').execute()
    items = results.get('files', [])

    if not items:
        return user.getstr('drive_list_no_files')
    else:
        print('Files:')
        text = user.getstr('drive_list_header')
        for item in items:
            text += '\n<b>{name}</b> • <code>{kind}</code>'.format(name=item.get('name'), kind=item.get('kind'))
        print(text)
        return text
