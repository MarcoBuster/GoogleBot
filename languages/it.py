AUTHOR = 'Marco Aceti'
AUTHOR_HREF = 'https://www.github.com/MarcoBuster/'
LANGUAGE = 'Italian'  # Must be in english
LANGUAGE_CODE = 'it'  # Must respect this: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

# TODO: Reorder strings

STRINGS = [
    {
        'start': '<b>Benvenuto nel bot</b>!\nStai usando la traduzione <b>italiana</b>',
        'sign_in': '👤 <b>Esegui il login con Google</b>'
                   '\nEseguendo il login con Google potrai sfruttare al massimo questo bot',
        'sign_in_button': '👤 Esegui il login con Google',
        'back_button': '🔙 Torna indietro',
        'news_button': '📰 Notizie',
        'settings_button': '⚙ Impostazioni',
        'settings': 'Che impostazione vuoi cambiare?',
        'trends_button': '📊 Trends',
        'trends': '🔍 Inserisci un <b>argomento</b> di cui vuoi visualizzarne le 📊  <b>statistiche</b>',
        'trends_not_found': '❌ <b>Nessun risultato trovato</b>\nProva a cercare qualcosa di meno specifico',
        'generating_graph': '🔄 <b>Sto generando il grafico...</b>',
        'generated_graph': '✅ <b>Grafico generato.</b>',
        'calendar_button': '📅 Calendario',
        'setlan_button': '⚙ Cambia lingua',
        'setlan': '<b>Seleziona la tua lingua</b> - Select your language',
        # -- Calendar plugin strings --
        # Events list
        'header': '📅 <b>Tutti i tuoi eventi sul calendario</b>',
        'event_by': 'creato da',
        'your_self': 'te stesso',
        'no_title': 'Nessun titolo',
        'start_event_time': 'dalle ore {hour} del giorno {date}',
        'end_event_time': 'alle ore {hour} del giorno {date}',
        'all_day_time': 'tutto il giorno {day}',
        'no_events': '📅 <b>Non ci sono eventi sul tuo calendario</b>',
        # -- Buttons --
        # Controls
        'first_page': '⏪ Prima pagina',
        'next_page': '▶️ Prossima pagina'
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
