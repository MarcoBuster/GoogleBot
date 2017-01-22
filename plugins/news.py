import feedparser
import bs4
from objects import callback, user


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


def process_callback(bot, chains, update):
    cb = callback.Callback(update)
    usr = user.User(cb.sender)

    if cb.query == 'news':
        if usr.exists:
            lang = usr.language()
        else:
            lang = 'en'

        bot.api.call('editMessageText', {
            'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': get(lang=lang), 'parse_mode': 'HTML',
            'reply_markup': '{"inline_keyboard": '
                            '[[{"text": "' + usr.getstr('back_button') + '", "callback_data": "home"}]]}'
        })
