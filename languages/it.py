AUTHOR = 'Marco Aceti'
AUTHOR_HREF = 'https://www.github.com/MarcoBuster/'
LANGUAGE = 'Italian'  # Must be in english
LANGUAGE_CODE = 'it'  # Must respect this: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

STRINGS = [
    {
        'start': '<b>Benvenuto nel bot</b>!\nStai usando la traduzione <b>italiana</b>',
        'back_button': '🔙 Torna indietro',
        'news_button': '📰 Notizie',
        'settings_button': '⚙ Impostazioni',
        'settings': 'Che impostazione vuoi cambiare?',
        'trends_button': '📊 Trends',
        'trends': '🔍 Inserisci un <b>argomento</b> di cui vuoi visualizzarne le 📊  <b>statistiche</b>',
        'generating_graph': '🔄 <b>Sto generando il grafico...</b>',
        'generated_graph': '✅ <b>Grafico generato.</b>',
        'setlan_button': '⚙ Cambia lingua',
        'setlan': '<b>Seleziona la tua lingua</b> - Select your language'
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
