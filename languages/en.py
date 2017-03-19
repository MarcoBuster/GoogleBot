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


AUTHOR = 'Marco Aceti'
AUTHOR_HREF = 'https://www.github.com/MarcoBuster/'
LANGUAGE = 'English'  # Must be in english
LANGUAGE_CODE = 'en'  # Must respect this: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

# TODO: Reorder strings

STRINGS = [
    {
        'start': '<b>Welcome to the bot!</b>\nYou are using the <b>English translation</b>.',
        'sign_in': '👤 <b>Sign in with Google</b>'
                   '\nSign in with Google to use this bot',
        'sign_in_button': '👤 Sign in with Google',
        'back_button': '🔙 Go back',
        'news_button': '📰 News',
        'settings_button': '⚙ Settings',
        'settings': 'What setting would you like to change?',
        'trends_button': '📊 Trends',
        'trends': '🔍 Insert a <b>query</b> you would to view the 📊  <b>stats</b> for',
        'trends_not_found': '❌ <b>No results</b>\nTry searching more general keywords',
        'generating_graph': '🔄 <b>I\'m generating the graph...</b>',
        'generated_graph': '✅ <b>Graph generated successfully.</b>',
        'calendar_button': '📅 Calendar',
        'setlang_button': '⚙ Change language',
        'setlang': '<b>Select your language</b>',
        # -- Initial setup strings --
        # Timezone
        'ask_timezone': 'Please, send me your location, I will determine your <b>timezone</b>',
        'ask_timezone_no_location': 'Please, send me your location from the attachments menu.',
        'ask_timezone_no_results': '<b>Invalid location</b>\nTry selecting a better known place!',
        # -- Calendar plugin strings --
        # Events list
        'header': '📅 <b>All the events in your calendar</b>',
        'event_by': 'created by',
        'your_self': 'yourself',
        'no_title': 'No title',
        'start_event_time': 'from hour {hour} of day {date}',
        'end_event_time': 'to hour {hour} of day {date}',
        'all_day_time': 'all day {day}',
        'no_events': '📅 <b>There aren\'t any events on your calendar</b>',
        # Create event
        'create_event_header': '📅  <b>Event creation</b>\n',
        'create_event_notext_error': '❌ The message <b>doesn\'t contain any text.</b>\nPlease, <b>try again.</b>',
        'create_event_timeformatting_error': '❌ <b>Error in the time\'s format</b>'
                                             '\nThe correct format is: <code>hh:mm dd/mm/yyy</code>'
                                             ' - <code>hh:mm dd/mm/yyyy</code>',
        'create_event_first_step': '1️⃣ <i>Insert the event\'s name</i>'
                                   '\nIf you want to add a <b>description</b>, add a dot'
                                   ' <code>.</code> at the end of the name,'
                                   ' followed by the description, for example:'
                                   '\n<code>Dinner with Clara. Remember to buy chocolates!</code>',
        'create_event_second_step': '2️⃣ <i>Enter the starting and ending time of your event</i>'
                                    '\nWrite the <b>starting</b> and <b>ending dates</b> of your event'
                                    ' in this format: <code>hh:mm dd/mm/yyyy</code>.'
                                    ' Put a dash <code>-</code> between the two, for example:'
                                    '\n<code>12:30 22/02/2017 - 13:10 22/02/2017</code>',
        'create_event_completed': '🆗 <i>Done!</i>'
                                  '\n<b>Event\'s name</b>: {name}'
                                  '{description}'
                                  '\n<a href="{url}">Click here to view the event on Google Calendar.</a>',
        'create_event_completed_description': '\n<b>Description</b>: {description}',
        # Update event
        'update_event': 'edit',
        'update_event_header': '📅  <b>Edit an event</b>\n',
        'update_event_first_step': '1️⃣ <i>Insert the event\'s new name</i>'
                                   '\nIf you want to add a <b>description</b>, add a dot'
                                   ' <code>.</code> at the end of the name,'
                                   ' followed by the description, for example:'
                                   '\n<code>Dinner with Clara. Remember to buy chocolates!</code>',
        'update_event_second_step': '2️⃣ <i>Enter the new starting and ending time of your event</i>'
                                    '\nWrite the <b>starting</b> and <b>ending dates</b> of your event'
                                    ' in this format: <code>hh:mm dd/mm/yyyy</code>.'
                                    ' Put a dash <code>-</code> between the two, for example:'
                                    '\n<code>12:30 22/02/2017 - 13:10 22/02/2017</code>',
        'update_event_completed': '🆗 <i>Done!</i>'
                                  '\n<b>Event\'s name</b>: {name}'
                                  '{description}'
                                  '\n<a href="{url}">Click here to view the event on Google Calendar.</a>',
        'update_event_completed_description': '\n<b>Description</b>: {description}',
        # Delete
        'deleted_event': '🗑 <b>Your event has been deleted.</b>',
        # -- Drive plugins strings --
        # List
        'drive_list_header': '📑 <b>Your files</b>',
        'drive_list_no_files': '❌ <b>No files found in your Google Drive account</b>',
        # Download
        'drive_download': 'download',  # Must be lowercase
        'drive_download_allfolder': 'download all files in this screen',  # Must be lowercase
        'drive_downloading_progress': 'Downloading your file... ({p}%)',
        'drive_downloading_uploading': 'Uploading your file in Telegram...',
        'drive_downloading_generic_error': 'Unable to download the file.',
        'drive_downloading_too_big': 'The file is too big for be sent in Telegram.',
        'drive_downloading_done': 'Done!',
        # Upload
        'drive_upload': '<b>Send a file and it\'ll uploaded in this folder!</b>',
        'drive_upload_button': '➕ Upload a file here',
        'drive_upload_no_file': '❌ <b>This is not a file.</b>'
                                '\nIf you are trying to send a photo, a video, a song, ..., <b>send it as a file</b>',
        'drive_upload_ask_name': '📝 <b>Come vuoi chiamare il file</b>?',
        'drive_uploading_progress': 'Uploading your file... ({p}%)',
        'drive_uploading_done': 'Done!',
        # -- Buttons --
        # Controls
        'first_page': '⏪ First page',
        'next_page': '▶️ Next page',
        # Calendar
        'add_event_button': '➕ Add an event',
        'edit_event_button': '✍️ Edit',
        'delete_event_button': '🗑 Delete',
        'update_event_same': '🙈 Keep like this',
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
