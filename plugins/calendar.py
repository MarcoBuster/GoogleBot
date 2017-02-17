import httplib2
from apiclient import discovery

from datetime import datetime
from objects import callback
from objects import user as _user

import logging
logger = logging.getLogger('testtt')


def login(user):
    credentials = user.credentials()
    http = credentials.authorize(httplib2.Http())
    return discovery.build('calendar', 'v3', http=http)


def formatevents(user, result):
    events = result.get('items', [])

    text = user.getstr('header')
    for event in events:
        start = datetime.strptime(event['start'].get('dateTime'), '%Y-%m-%dT%H:%M:%S+%f:00')
        end = datetime.strptime(event['end'].get('dateTime'), '%Y-%m-%dT%H:%M:%S+%f:00')
        date = (
            user.getstr('start_event_time').format(hour=start.strftime('%H:%M'), date=start.strftime('%d/%m/%y')) +
            ' ' + user.getstr('end_event_time').format(hour=end.strftime('%H:%M'), date=end.strftime('%d/%m/%y')))

        location, description = '', ''
        creator = event.get('creator').get('displayName')

        if event.get('location', None) is not None:
            location = '• ' + event.get('location')

        if event.get('description', None) is not None and event.get('description', None) != event.get('summary'):
            description = '\n<i>{description}</i>'.format(description=event.get('description'))

        if event.get('creator').get('self'):
            creator = user.getstr('your_self')

        text += (
            '\n🔸 <b>{title}</b> • {by} {creator} • {date} {location} {description}\n'.format(
                title=event.get('summary', user.getstr('no_title')), by=user.getstr('event_by'), creator=creator,
                date=date, location=location, description=description
            )
        )
        del event  # Temporary fix for dict.get() bug (or feature?)
    return text


def getevents(user, elements_range):
    logger.info('Funzione getEvents richiamata')
    service = login(user)
    logger.info('logged innn')

    command = service.events().list(
        calendarId='primary', timeMin=datetime.utcnow().isoformat() + 'Z',
        maxResults=elements_range[1], singleEvents=True, orderBy='startTime', pageToken=elements_range[0]
    )
    result = command.execute()
    logger.info('commanddo eseguito badrone')
    text = formatevents(user, result)
    logger.info('risposta formattata +++')
    pagetoken = result.get('nextPageToken', None)

    if elements_range[0] is not None:
        firstpage = '{"text": "' + user.getstr('first_page') + '", "callback_data": "cd@list@first"}'
    else:
        firstpage = ''
    if pagetoken is not None:
        nextpage = '{"text": "' + user.getstr('next_page') + '", "callback_data": "cd@list@' + pagetoken + '"}'
    else:
        nextpage = ''
    if firstpage == '' and nextpage == '':
        br1, br2 = '', ''
    else:
        br1 = '['
        br2 = '], '

    inline_keyboard = '{"inline_keyboard": ' \
                      '[' + br1 + firstpage + (',' if firstpage != '' and nextpage != '' else '') + nextpage \
                      + br2 + '[{"text": "' + user.getstr('back_button') + '", "callback_data": "home"}]]}'
    print(inline_keyboard)
    return text, inline_keyboard


def process_callback(bot, chains, update):
    cb = callback.Callback(update)
    print(cb.query)
    user = _user.User(cb.sender)

    if 'cd@' in cb.query:
        if 'cd@list@' in cb.query:
            page = cb.query.replace('cd@list@', '')

            if page == "first":
                text, inline_keyboard = getevents(user, elements_range=[None, 3])
            else:
                text, inline_keyboard = getevents(user, elements_range=[page, 3])

            bot.api.call('editMessageText',
                         {'chat_id': cb.chat.id, 'message_id': cb.message.message_id,
                          'text': text, 'parse_mode': 'HTML',
                          'reply_markup': inline_keyboard
                          })
