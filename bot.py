"""
Copyright (c) 2017 Marco Aceti <dev@marcoaceti.it>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import sqlite3

import botogram.objects.base
import botogram

from config import *
from objects import callback, user, message_update
from plugins import news, trends, calendar, drive

from oauth import oauth

import googlemaps
from config import GOOGLE_API_KEY

import json

import os
import subprocess
subprocess.Popen(['python3', 'callback_handler.py'])

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)


class CallbackQuery(botogram.objects.base.BaseObject):
    required = {
        "id": str,
        "from": botogram.User,
        "data": str,
    }
    optional = {
        "inline_message_id": str,
        "message": botogram.Message,
    }
    replace_keys = {
        "from": "sender"
    }


botogram.Update.optional["callback_query"] = CallbackQuery

bot = botogram.create(TOKEN)
bot.process_backlog = True

conn = sqlite3.connect('users.sqlite')
c = conn.cursor()


def process_callback(bot, chains, update):
    cb = callback.Callback(update)
    usr = user.User(cb.sender)

    if 'l@' in cb.query:
        usr.language(new_language=cb.query.replace('l@', ''))
        if usr.logged_in:
            cb.query = 'home'

    if not usr.logged_in and usr.exists:
        bot.api.call('editMessageText', {
            'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': usr.getstr('sign_in'),
            'parse_mode': 'HTML', 'reply_markup':
                json.dumps(
                    {'inline_keyboard': [
                        [{"text": usr.getstr('sign_in_button'), "url": oauth.get_url()}]
                    ]}
            )
        })
        return

    if cb.query == 'sign_in':
        bot.api.call("answerCallbackQuery", {
            'callback_query_id': cb.id, 'url': 'telegram.me/your_bot?start=XXXX'
        })

    if not usr.exists:
        text = (
            "<b>Welcome!</b>"
            "\nFirst, <b>select your language</b>:"
        )
        bot.api.call('editMessageText', {
            'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': text,
            'parse_mode': 'HTML', 'reply_markup':
                json.dumps(
                    {'inline_keyboard': [
                        [{"text": "🇮🇹 Italian", "callback_data": "l@it"},
                         {"text": "🇬🇧 English", "callback_data": "l@en"},
                         {"text": "🇪🇸 Spanish", "callback_data": "l@es"}]
                    ]}
                )
        })

    if cb.query == 'home':
        bot.api.call('editMessageText', {
            'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': usr.getstr('start'),
            'parse_mode': 'HTML', 'reply_markup':
                json.dumps(
                    {"inline_keyboard": [
                        [{"text": usr.getstr('news_button'), "callback_data": "news"},
                         {"text": usr.getstr('trends_button'), "callback_data": "trends"},
                         {"text": usr.getstr('calendar_button'), "callback_data": "calendar"}],
                        [{"text": usr.getstr('drive_button'), "callback_data": "drive"}],
                        [{"text": usr.getstr('settings_button'), "callback_data": "settings"}],
                    ]}
            )
        })

    elif cb.query == 'settings':
        bot.api.call('editMessageText', {
            'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': usr.getstr('settings'),
            'parse_mode': 'HTML', 'reply_markup':
                json.dumps(
                    {'inline_keyboard': [
                        [{"text": usr.getstr('setlang_button'), "callback_data": "setlang"}],
                        [{"text": usr.getstr('back_button'), "callback_data": "home"}]
                    ]}
            )
        })

    elif cb.query == 'setlang':
        bot.api.call('editMessageText', {
            'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': usr.getstr('setlang'),
            'parse_mode': 'HTML', 'reply_markup':
                json.dumps(
                    {'inline_keyboard': [
                        [{"text": "🇮🇹 Italian", "callback_data": "l@it"},
                         {"text": "🇬🇧 English", "callback_data": "l@en"},
                         {"text": "🇪🇸 Spanish", "callback_data": "l@es"}]
                    ]}
            )
        })

    elif cb.query == 'trends':
        usr.state(new_state='trends1')
        bot.api.call('editMessageText', {
            'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': usr.getstr('trends'),
            'parse_mode': 'HTML', 'reply_markup':
                json.dumps(
                    {'inline_keyboard': [
                        [{"text": usr.getstr('back_button'), "callback_data": "home"}]
                    ]}
            )
        })

    elif cb.query == 'calendar':
        text, inline_keyboard = calendar.getevents(usr, [None, 3])
        bot.api.call('editMessageText', {
            'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': text,
            'parse_mode': 'HTML', 'disable_web_page_preview': True, 'reply_markup': inline_keyboard
        })

    elif cb.query == 'drive':
        text, inline_keyboard = drive.getfiles(user=usr, pagetoken=None, parent='root')
        bot.api.call('editMessageText', {
            'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': text,
            'parse_mode': 'HTML', 'disable_web_page_preview': True, 'reply_markup': inline_keyboard
        })

    news.process_callback(bot, cb, usr)
    calendar.process_callback(bot, cb, usr)
    drive.process_callback(bot, cb, usr)


bot.register_update_processor("callback_query", process_callback)


@bot.command("start")
def start(chat, message, args):
    usr = user.User(message.sender)
    usr.state('home')

    if 'oauth-' in ''.join(args):
        short_code = ''.join(args).replace('oauth-', '')
        c.execute('SELECT code FROM cache_oauth_codes WHERE short_code=?', (short_code,))
        code = c.fetchone()[0]
        oauth.save(usr, code)

        c.execute('DELETE FROM cache_oauth_codes WHERE code=?', (code,))
        conn.commit()

    if 'cd-edit-' in ''.join(args):
        short_event_id = ''.join(args).replace('cd-edit-', '')
        c.execute('SELECT id FROM cache_calendar_event_ids WHERE short_id=?', (short_event_id,))
        event_id = c.fetchone()[0]

        text = calendar.formatevent(usr, event_id)
        bot.api.call('sendMessage', {
            'chat_id': chat.id, 'text': text, 'parse_mode': 'HTML', 'reply_markup':
                json.dumps(
                    {'inline_keyboard': [
                        [{"text": usr.getstr('edit_event_button'), "callback_data": "cd@edit@" + short_event_id},
                         {"text": usr.getstr('delete_event_button'), "callback_data": "cd@delete@" + short_event_id}],
                        [{"text": usr.getstr('back_button'), "callback_data": "home"}]
                    ]}
                )
        })
        return True

    if 'drv-file-' in ''.join(args):
        if '-download' in ''.join(args):
            args = ''.join(args)
            file = args.lstrip('drv-file').rstrip('-download')

            msg = chat.send(usr.getstr('drive_downloading_progress').format(p=0))
            try:
                filename = drive.download(usr, drive.getfile(usr, file), msg)
            except:
                msg.edit('Unable to download the file.')
                return

            msg.edit(usr.getstr('drive_downloading_uploading'))

            if os.path.getsize(filename) > 50000000:
                msg.edit('File is too big for be sent.')
                return

            if filename.endswith('.png') or filename.endswith('.jpg'):
                message.reply_with_photo(filename)
            elif filename.endswith('.mp3'):
                message.reply_with_audio(filename)
            elif filename.endswith('.ogg'):
                message.reply_with_voice(filename)
            else:
                message.reply_with_file(filename)

            msg.edit(usr.getstr('drive_downloading_done'))
            os.remove(filename)
            return

        if '-delete' in ''.join(args):
            args = ''.join(args)
            file = args.lstrip('drv-file').rstrip('-delete')

            bot.api.call('sendMessage', {
                'chat_id': chat.id, 'text': usr.getstr('drive_delete_confirm'),
                'parse_mode': 'HTML', 'reply_markup':
                    json.dumps(
                        {"inline_keyboard": [
                            [{"text": usr.getstr('drive_delete_button'),
                              "callback_data": "drv@file@" + file + "@delete"},
                             {"text": usr.getstr('back_button'), "callback_data": "drive"}]
                        ]}
                    )
            })
            return

    if not usr.exists:
        text = (
            "<b>Welcome!</b>"
            "\nFirst, <b>select your language</b>:"
        )
        bot.api.call('sendMessage', {
            'chat_id': chat.id, 'text': text,
            'parse_mode': 'HTML', 'reply_markup':
                json.dumps(
                    {'inline_keyboard': [
                        [{"text": "🇮🇹 Italian", "callback_data": "l@it"},
                         {"text": "🇬🇧 English", "callback_data": "l@en"},
                         {"text": "🇪🇸 Spanish", "callback_data": "l@es"}]
                    ]}
                )
        })
        return

    if not usr.timezone():
        chat.send(usr.getstr('ask_timezone'))
        usr.state('timezone')
        return

    bot.api.call('sendMessage', {
        'chat_id': chat.id, 'text': usr.getstr('start'), 'parse_mode': 'HTML', 'reply_markup':
            json.dumps(
                {"inline_keyboard": [
                    [{"text": usr.getstr('news_button'), "callback_data": "news"},
                     {"text": usr.getstr('trends_button'), "callback_data": "trends"},
                     {"text": usr.getstr('calendar_button'), "callback_data": "calendar"}],
                    [{"text": usr.getstr('drive_button'), "callback_data": "drive"}],
                    [{"text": usr.getstr('settings_button'), "callback_data": "settings"}]
                ]}
            )
    })


@bot.process_message
def process_message(message, chat):
    usr = user.User(message.sender)

    if usr.state() == 'timezone':
        if message.location is None:
            message.reply(usr.getstr('ask_timezone_no_location'))
            return True

        lat = message.location.latitude
        lon = message.location.longitude
        result = gmaps.timezone([lat, lon]).get('timeZoneId', False)
        if not result:
            message.reply(usr.getstr('ask_timezone_no_results'))
            return True

        usr.timezone(result)
        start(chat, message, args=[])

    update = message_update.MessageUpdate(usr, bot, chat, message)
    trends.process_message(update)
    calendar.process_message(update)
    drive.process_message(update)

if __name__ == '__main__':
    bot.run(workers=10)
