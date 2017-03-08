from apiclient import discovery
import httplib2

import json

import random
import string

import sqlite3

conn = sqlite3.connect('users.sqlite')
c = conn.cursor()


def login(user):
    credentials = user.credentials()
    http = credentials.authorize(httplib2.Http())
    return discovery.build('drive', 'v3', http=http)


def getfiles(user, pagetoken=None, parent=None):
    service = login(user)
    results = service.files().list(
        pageSize=10, orderBy='folder', pageToken=pagetoken,
        q='"{parent}" in parents'.format(parent=parent) if parent is not None else '').execute()
    items = results.get('files', [])

    if not items:
        # TODO: Custom error message for each folder

        return user.getstr('drive_list_no_files'), \
               json.dumps(
                   {"inline_keyboard": [[{"text": user.getstr('back_button'), "callback_data": "home"}]]}
               )

    text = user.getstr('drive_list_header')  # TODO: Custom header for each folder
    reply_markup = {"inline_keyboard": [[{"foo": "bar"}]]}
    for item in items:  # TODO: Better listing design
        if item.get('mimeType') == 'application/vnd.google-apps.folder':
            reply_markup["inline_keyboard"] += [[{"text": '➡️ 📂' + item.get('name'),
                                                "callback_data": "drv@fldr@" + item.get('id')}]]
            text += '\n📂 <b>{name}</b>'.format(name=item.get('name'))
        else:
            text += '\n📃 <b>{name}</b>'.format(name=item.get('name'))

    del reply_markup["inline_keyboard"][0]

    if results.get('nextPageToken') is not None:
        next_page_token = results.get('nextPageToken')
        short_token = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
        c.execute('INSERT INTO cache_drive_page_tokens VALUES(?, ?)', (next_page_token, short_token))
        conn.commit()

        # TODO: First and previous page button

        reply_markup["inline_keyboard"] += \
            [[{"text": user.getstr('next_page'), "callback_data": "drv@fldr@" + parent + "@page@" + short_token}]]

    reply_markup["inline_keyboard"] += \
        [[{"text": user.getstr('back_button'), "callback_data": "drive" if parent != 'root' else "home"}]]

    # TODO: Go to upper folder by pressing back button

    return text, json.dumps(reply_markup)


def process_callback(bot, cb, user):
    if 'drv@' in cb.query:
        if 'drv@fldr@' in cb.query:
            if '@page' in cb.query:
                parent = cb.query.split('@')[2]
                short_token = cb.query.split('@')[4]

                c.execute('SELECT token FROM cache_drive_page_tokens WHERE short_token=?', (short_token,))
                next_page_token = c.fetchone()[0]

                c.execute('DELETE FROM cache_drive_page_tokens WHERE short_token=?', (short_token,))
                conn.commit()

                text, inline_keyboard = getfiles(user, pagetoken=next_page_token, parent=parent)
                bot.api.call('editMessageText', {
                    'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': text,
                    'parse_mode': 'HTML', 'disable_web_page_preview': True, 'reply_markup': inline_keyboard
                })
                return

            text, inline_keyboard = getfiles(user, pagetoken=None, parent=cb.query.lstrip('drv@fldr@'))
            bot.api.call('editMessageText', {
                'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': text,
                'parse_mode': 'HTML', 'disable_web_page_preview': True, 'reply_markup': inline_keyboard
            })
