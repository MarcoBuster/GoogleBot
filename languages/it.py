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
        # Create event
        'create_event_header': '📅  <b>Creazione di un evento</b>\n',
        'create_event_notext_error': '❌ Il messaggio <b>non contiene testo</b>\nPer favore, <b>riprova</b>',
        'create_event_timeformatting_error': '❌ <b>Errore nella formattazione dell\'orario</b>'
                                             '\nRicorda che il formato è: <code>ora:minuto giorno/mese/anno</code>'
                                             ' - <code>ora:minuto giorno/mese/anno</code>',
        'create_event_first_step': '1️⃣ <i>Inserisci il nome dell\'evento</i>'
                                   '\nSe vuoi aggiungere una <b>descrizione</b>, aggiungi alla fine'
                                   ' un punto <code>.</code>'
                                   ' seguito dalla tua descrizione, per esempio:'
                                   '\n<code>Cena con Clara. Ricordati di comprare i cioccolatini!</code>',
        'create_event_second_step': '2️⃣ <i>Inserisci l\'ora di inizio e di fine del tuo evento</i>'
                                    '\nScrivi la <b>data di inizio</b> e <b>di fine</b> del tuo evento'
                                    ' in questo formato: <code>ora:minuto giorno/mese/anno</code>,'
                                    ' mettendoci un trattino <code>-</code> in mezzo, per esempio:'
                                    '\n<code>12:30 22/02/2017 - 13:10 22/02/2017</code>',
        'create_event_completed': '🆗 <i>Fatto!</i>'
                                  '\n<b>Nome dell\'evento</b>: {name}'
                                  '{description}'
                                  '\n<a href="{url}">Clicca qui per visualizzare l\'evento su Calendari Google</a>',
        'create_event_completed_description': '\n<b>Descrizione</b>: {description}',
        # Update event
        'update_event': 'modifica',
        'update_event_header': '📅  <b>Modifica di un evento</b>\n',
        'update_event_first_step': '1️⃣ <i>Inserisci il nuovo nome dell\'evento</i>'
                                   '\nSe vuoi aggiungere una <b>descrizione</b>, aggiungi alla fine'
                                   ' un punto <code>.</code>'
                                   ' seguito dalla tua descrizione, per esempio:'
                                    '\n<code>Cena con Clara. Ricordati di comprare i cioccolatini!</code>',
        'update_event_second_step': '2️⃣ <i>Inserisci la nuova ora di inizio e di fine del tuo evento</i>'
                                    '\nScrivi la <b>data di inizio</b> e <b>di fine</b> del tuo evento'
                                    ' in questo formato: <code>ora:minuto giorno/mese/anno</code>,'
                                    ' mettendoci un trattino <code>-</code> in mezzo, per esempio:'
                                    '\n<code>12:30 22/02/2017 - 13:10 22/02/2017</code>',
        'update_event_completed': '🆗 <i>Fatto!</i>'
                                  '\n<b>Nome dell\'evento</b>: {name}'
                                  '{description}'
                                  '\n<a href="{url}">Clicca qui per visualizzare l\'evento su Calendari Google</a>',
        'update_event_completed_description': '\n<b>Descrizione</b>: {description}',
        # Delete
        'deleted_event': '🗑 <b>Il tuo evento è stato eliminato con successo</b>',
        # -- Buttons --
        # Controls
        'first_page': '⏪ Prima pagina',
        'next_page': '▶️ Prossima pagina',
        # Calendar
        'add_event_button': '➕ Aggiungi un evento',
        'edit_event_button': '✍️ Modifica',
        'delete_event_button': '🗑 Elimina',
        'update_event_same': '🙈 Lascia così'
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
