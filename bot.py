import botogram.objects.base
import botogram
import os

from config import *
from objects import callback, user
from plugins import news, trends


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
        bot.api.call('editMessageText',
                     {'chat_id': cb.chat.id, 'message_id': cb.message.message_id,
                      'text': usr.getstr('start'), 'parse_mode': 'HTML',
                      'reply_markup': '{"inline_keyboard": '
                                      '[[{"text": "' + usr.getstr('news_button') + '", "callback_data": "news"},'
                                                                                   '{"text": "' + usr.getstr(
                          'trends_button') + '", "callback_data": "trends"}],'
                                             '[{"text": "' + usr.getstr(
                          'settings_button') + '", "callback_data": "settings"}]]}'
                      })

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
                          'trends_button') + '", "callback_data": "trends"}],'
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
                                      '[{"text": "'+usr.getstr('back_button')+'", "callback_data": "home"}]]}'
                      })

    news.process_callback(bot, chains, update)


bot.register_update_processor("callback_query", process_callback)


@bot.command("start")
def start(chat, message):
    usr = user.User(message.sender)
    usr.state('home')

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
                        '{"text": "'+usr.getstr('trends_button')+'", "callback_data": "trends"}],'
                        '[{"text": "' + usr.getstr('settings_button') + '", "callback_data": "settings"}]]}'
    })


@bot.process_message
def process_message(chat, message):
    usr = user.User(message.sender)

    if message.text is None:
        return True

    if usr.state() == 'home':
        return True

    elif usr.state() == 'trends1':
        msg = message.reply(usr.getstr('generating_graph'))
        file = trends.graph(message.text)
        message.reply_with_photo(file)
        os.remove(file)  # Disk space is sacred
        msg.edit(usr.getstr('generated_graph'))

if __name__ == '__main__':
    bot.run()
