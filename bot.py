import botogram.objects.base
import botogram

from config import *
from objects import callback, user, message_update
from plugins import news, trends, calendar

from oauth import oauth


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


def process_callback(bot, chains, update):
    cb = callback.Callback(update)
    usr = user.User(cb.sender)

    if 'l@' in cb.query:
        usr.language(new_language=cb.query.replace('l@', ''))
        if usr.logged_in:
            cb.query = 'home'

    if not usr.logged_in and usr.exists:
        bot.api.call('editMessageText',
                     {'chat_id': cb.chat.id, 'message_id': cb.message.message_id,
                      'text': usr.getstr('sign_in'), 'parse_mode': 'HTML',
                      'reply_markup': '{"inline_keyboard": '
                                      '[[{"text": '
                                      '"' + usr.getstr('sign_in_button') + '",'
                                                                           ' "url": "' + oauth.get_url() + '"}]]}'
                      })
        return

    if cb.query == 'sign_in':
        bot.api.call("answerCallbackQuery",
                     {'callback_query_id': cb.id, 'url': 'telegram.me/your_bot?start=XXXX'})

    if not usr.exists:
        text = (
            "<b>Welcome!</b>"
            "\nFirst, <b>select your language</b>:"
        )
        bot.api.call('editMessageText',
                     {'chat_id': cb.chat.id, 'message_id': cb.message.message_id,
                      'text': text, 'parse_mode': 'HTML',
                      'reply_markup': '{"inline_keyboard": ['
                                      '[{"text": "🇮🇹 Italian", "callback_data": "l@it"},'
                                      '{"text": "🇬🇧 English", "callback_data": "l@en"}]]}'
                      })

    if cb.query == 'home':
        bot.api.call('editMessageText',
                     {'chat_id': cb.chat.id, 'message_id': cb.message.message_id,
                      'text': usr.getstr('start'), 'parse_mode': 'HTML',
                      'reply_markup': '{"inline_keyboard": '
                                      '[[{"text": "' + usr.getstr('news_button') + '", "callback_data": "news"},'
                                                                                   '{"text": "' + usr.getstr(
                          'trends_button') + '", "callback_data": "trends"},'
                                             '{"text": "' + usr.getstr(
                          'calendar_button') + '", "callback_data": "calendar"}],'
                                               '[{"text": "' + usr.getstr(
                          'settings_button') + '", "callback_data": "settings"}]]}'
                      })

    elif cb.query == 'settings':
        bot.api.call('editMessageText',
                     {'chat_id': cb.chat.id, 'message_id': cb.message.message_id,
                      'text': usr.getstr('settings'), 'parse_mode': 'HTML',
                      'reply_markup': '{"inline_keyboard": '
                                      '[[{"text": "' + usr.getstr('setlan_button') + '", "callback_data": "setlan"}]]}'
                      })

    elif cb.query == 'setlan':
        bot.api.call('editMessageText',
                     {'chat_id': cb.chat.id, 'message_id': cb.message.message_id,
                      'text': usr.getstr('setlan'), 'parse_mode': 'HTML',
                      'reply_markup': '{"inline_keyboard": ['
                                      '[{"text": "🇮🇹 Italian", "callback_data": "l@it"},'
                                      '{"text": "🇬🇧 English", "callback_data": "l@en"}]]}'
                      })

    elif cb.query == 'trends':
        usr.state(new_state='trends1')
        bot.api.call('editMessageText',
                     {'chat_id': cb.chat.id, 'message_id': cb.message.message_id,
                      'text': usr.getstr('trends'), 'parse_mode': 'HTML',
                      'reply_markup': '{"inline_keyboard": ['
                                      '[{"text": "' + usr.getstr('back_button') + '", "callback_data": "home"}]]}'
                      })

    elif cb.query == 'calendar':
        text, inline_keyboard = calendar.getevents(usr, [None, 3])
        bot.api.call('editMessageText',
                     {'chat_id': cb.chat.id, 'message_id': cb.message.message_id,
                      'text': text, 'parse_mode': 'HTML', 'disable_web_page_preview': True,
                      'reply_markup': inline_keyboard
                      })

    news.process_callback(bot, cb, usr)
    calendar.process_callback(bot, cb, usr)


bot.register_update_processor("callback_query", process_callback)


@bot.command("start")
def start(chat, message, args):
    usr = user.User(message.sender)
    usr.state('home')

    if 'oauth@' in ''.join(args):
        oauth.save(usr, ''.join(args).replace('oauth@', ''))

    if 'cd@edit@' in ''.join(args):
        event_id = ''.join(args).replace('cd@edit@', '')
        text = calendar.formatevent(usr, event_id)
        bot.api.call('sendMessage', {
            'chat_id': chat.id, 'text': text, 'parse_mode': 'HTML', 'reply_markup':
                '{"inline_keyboard":'
                '[[{"text": "' + usr.getstr('edit_event_button') + '", "callback_data": "cd@edit@' + event_id + '"},'
                '{"text": "' + usr.getstr('delete_event_button') + '", "callback_data": "cd@delete@' + event_id + '"}],'
                '[{"text": "' + usr.getstr('back_button') + '", "callback_data": "home"}]]}'
        })
        return True

    if not usr.exists:
        text = (
            "<b>Welcome!</b>"
            "\nFirst, <b>select your language</b>:"
        )
        bot.api.call('sendMessage',
                     {'chat_id': chat.id, 'text': text, 'parse_mode': 'HTML',
                      'reply_markup': '{"inline_keyboard": ['
                                      '[{"text": "🇮🇹 Italian", "callback_data": "l@it"},'
                                      '{"text": "🇬🇧 English", "callback_data": "l@en"}]]}'
                      })
        return

    bot.api.call('sendMessage', {
        'chat_id': chat.id,
        'text': usr.getstr('start'), 'parse_mode': 'HTML',
        'reply_markup': '{"inline_keyboard": '
                        '[[{"text": "' + usr.getstr('news_button') + '", "callback_data": "news"},'
                                                                     '{"text": "' + usr.getstr(
            'trends_button') + '", "callback_data": "trends"},'
                               '{"text": "' + usr.getstr('calendar_button') + '", "callback_data": "calendar"}],'
                                                                              '[{"text": "' + usr.getstr(
            'settings_button') + '", "callback_data": "settings"}]]}'
    })


@bot.process_message
def process_message(message, chat):
    usr = user.User(message.sender)

    update = message_update.MessageUpdate(usr, bot, chat, message)
    trends.process_message(update)
    calendar.process_message(update)

if __name__ == '__main__':
    bot.run()
