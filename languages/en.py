AUTHOR = 'Marco Aceti'
AUTHOR_HREF = 'https://www.github.com/MarcoBuster/'
LANGUAGE = 'English'  # Must be in english
LANGUAGE_CODE = 'en'  # Must respect this: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

STRINGS = [
    {
        'start': '<b>Welcome in the bot!</b>\nYou are using <b>english translation</b>.',
        'sign_in': '👤 <b>Sign in with Google</b>'
                   '\nSign in with Google for use this bot',
        'sign_in_button': '👤 Sign in with Google',
        'back_button': '🔙 Return back',
        'news_button': '📰 News',
        'settings_button': '⚙ Settings',
        'settings': 'What setting do you want to change?',
        'trends_button': '📊 Trends',
        'trends': '🔍 Insert an <b>argument</b> that you would to view the 📊  <b>stats</b>',
        'trends_not_found': '❌ <b>No results</b>\nTry to search more general things',
        'generating_graph': '🔄 <b>I\'m generating the graph...</b>',
        'generated_graph': '✅ <b>Graph generated successfully.</b>',
        'calendar_button': '📅 Calendar',
        'setlan_button': '⚙ Change language',
        'setlan': '<b>Select new language</b>'
    }
]


def get(str_code):
    """Do not edit below, please"""
    for string in STRINGS:
        for key in string:
            if key == str_code:
                return string[key]

        return (
            'Error in translation:'
            '\nAuthor: {a} ({h})'
            '\nLanguage: {l} ({c})'
            '\nRequested string: {r}'.format(a=AUTHOR, h=AUTHOR_HREF, l=LANGUAGE, c=LANGUAGE_CODE, r=str_code)
        )
