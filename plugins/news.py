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


import feedparser
import bs4

import json


def get(query='', lang='en'):
    d = feedparser.parse('https://news.google.it/news?cf=all&hl={l}&query={q}&pz=1&ned={l}&output=rss'
                         .format(l=lang, q=query))
    text = d.feed.title
    for e in d.entries:
        soup = bs4.BeautifulSoup(e.description, 'html.parser')
        news = soup.find_all('font', size="-1")[1].get_text()
        title = e.title.rsplit('-')[0]
        author = e.title.rsplit('-')[1]
        title, author = title.rstrip().lstrip(), author.rstrip().lstrip()
        link = e.link
        text += (
            '\n📰 <b>{title}</b> • <a href="{link}">{author}</a>'
            '\n{news}\n'.format(title=title, news=news, link=link, author=author)
        )

    return text


def process_callback(bot, cb, usr):
    if cb.query == 'news':
        if usr.exists:
            lang = usr.language()
        else:
            lang = 'en'

        bot.api.call('editMessageText', {
            'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': get(lang=lang),
            'parse_mode': 'HTML', 'reply_markup':
            json.dumps(
                {"inline_keyboard": [
                    [{"text": usr.getstr('back_button'), "callback_data": "home"}]
                ]}
            )
        })
