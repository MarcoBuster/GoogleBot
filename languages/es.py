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


AUTHOR = 'Alessandro Casnigo'
AUTHOR_HREF = 'https://www.github.com/casungo/'
LANGUAGE = 'Spanish'  # Must be in english
LANGUAGE_CODE = 'es'  # Must respect this: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

# TODO: Reorder strings

STRINGS = [
    {
        'start': '<b>Bienvenida</b>!\nEstà utilizando una traducion <b>española</b>',
        'sign_in': '👤 <b>Tienes que hacer el login con Google</b>'
                   '\nRealizando el login con Google usted utilizar esto bot de mas',
        'sign_in_button': '👤 Realiza el login',
        'back_button': '🔙 Espalda',
        'news_button': '📰 Noticias',
        'settings_button': '⚙ Ajustes',
        'settings': '¿Que ajustacion tiene que modificar?',
        'trends_button': '📊 Trends',
        'trends': '🔍 Entra un <b>argomiento</b> que vuelves visualizar las 📊  <b>statistiche</b>',
        'trends_not_found': '❌ <b>Nadie resultado</b>',
        'generating_graph': '🔄 <b>Generacion de el grafico...</b>',
        'generated_graph': '✅ <b>Grafico generado.</b>',
        'calendar_button': '📅 Calendario',
        'setlang_button': '⚙ Cambia el idioma',
        'setlang': '<b>Selecciona tu idioma</b> - Select your language',
        # -- Initial setup strings --
        # Timezone
        'ask_timezone': 'Por favor, envia ahora tu ubicacion para identificar tu <b>huso horario</b>',
        'ask_timezone_no_location': 'Por favor, envia tu ubicacion da el menù adjuntos',
        'ask_timezone_no_results': '<b>Ubicacion invalida</b>',
        # -- Calendar plugin strings --
        # Events list
        'header': '📅 <b>Todos los eventos en el calendario</b>',
        'event_by': 'creado da',
        'your_self': 'usted mismo',
        'no_title': 'Ninguno titulo',
        'start_event_time': 'desde las {hour} de {date}',
        'end_event_time': 'a las {hour} de {date}',
        'all_day_time': 'todo el dia {day}',
        'no_events': '📅 <b>Ninguno evento en tu calendario</b>',
        # Create event
        'create_event_header': '📅  <b>Creacion de evento</b>\n',
        'create_event_notext_error': '❌ El mensaje <b>no contiene texto</b>\n<b>Inténtelo de nuevo</b>',
        'create_event_timeformatting_error': '❌ <b>Error en el formateo de tiempo</b>'
                                             '\nRecuerdate que el formato es: <code>hora:minutos dia/mes/año</code>'
                                             ' - <code>hora:minutos dia/mes/año</code>',
        'create_event_first_step': '1️⃣ <i>Entra el nombre de evento</i>'
                                   '\nSi vuelves añadir una <b>descripcion</b>, añadie a la fin de el texto'
                                   ' un punto <code>.</code>'
                                   ' por ejemplo:'
                                   '\n<code>Reunion con Alejandro. Requerdate la presentacion!</code>',
        'create_event_second_step': '2️⃣ <i>Entra el tiempo de inicio y de fin</i>'
                                    '\nEscribelo en esto formateo: <code>hora:minutos dia/mes/año</code>,'
                                    ' añadiendo <code>-</code> en el medio, por ejemplo:'
                                    '\n<code>12:30 22/02/2017 - 13:10 22/02/2017</code>',
        'create_event_completed': '🆗 <i>Hecho!</i>'
                                  '\n<b>Nombre de evento</b>: {name}'
                                  '{description}'
                                  '\n<a href="{url}">Click aqui por visualizar el evento en Calendario Google</a>',
        'create_event_completed_description': '\n<b>Descripcion</b>: {description}',
        # Update event
        'update_event': 'modifica',
        'update_event_header': '📅  <b>Modifica el evento</b>\n',
        'update_event_first_step': '1️⃣ <i>Entra el nombre de evento</i>'
                                   '\nSi vuelves añadir una <b>descripcion</b>, añadie a la fin de el texto'
                                   ' un punto <code>.</code>'
                                   ' por ejemplo:'
                                   '\n<code>Reunion con Alejandro. Requerdate la presentacion!</code>',
        'update_event_second_step': '2️⃣ <i>Entra el tiempo de inicio y de fin</i>'
                                    '\nEscribelo en esto formateo: <code>hora:minutos dia/mes/año</code>,'
                                    ' añadiendo <code>-</code> en el medio, por ejemplo:'
                                    '\n<code>12:30 22/02/2017 - 13:10 22/02/2017</code>',
        'update_event_completed': '🆗 <i>Hecho!</i>'
                                  '\n<b>Nombre de evento</b>: {name}'
                                  '{description}'
                                  '\n<a href="{url}">Click aqui por visualizar el evento en Calendario Google</a>',
        'update_event_completed_description': '\n<b>Descripcion</b>: {description}',
        # Delete
        'deleted_event': '🗑 <b>Tu evento es cancelado con exito</b>',
        # -- Drive plugins strings --
        # List
        'drive_list_header': '📂 <b>Tu file</b>',
        'drive_list_no_files': '❌ <b>Nadie file en tu Google Drive account</b>',
        # Download
        'drive_download': 'download',  # Must be lowercase
        'drive_download_allfolder': 'download all files in this screen',  # Must be lowercase
        'drive_downloading_progress': 'Downloading your file... ({p}%)',
        'drive_downloading_uploading': 'Uploading your file in Telegram...',
        'drive_downloading_generic_error': 'Unable to download the file.',
        'drive_downloading_too_big': 'The file is too big for be sent in Telegram.',
        'drive_downloading_done': 'Done!',
        # Upload
        'drive_uploading_progress': 'Uploading your file... ({p}%)',
        'drive_uploading_done': 'Done!',
        # -- Buttons --
        # Controls
        'first_page': '⏪ Primera pagina',
        'next_page': '▶️ Página siguiente',
        # Calendar
        'add_event_button': '➕ Añadie un evento',
        'edit_event_button': '✍️ Modifica',
        'delete_event_button': '🗑 Elimina',
        'update_event_same': '🙈 Deja asì',
        # Drive
        'drive_button': '📑 Drive'
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
