import sqlite3


class Callback:
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    def __init__(self, update):
        self.update = update.callback_query
        self.id = self.update.id
        self.query = self.update.data
        self.sender = self.update.sender
        self.message = self.update.message
        self.chat = self.message.chat

        if self.chat is None:
            self.isInline = True
        else:
            self.isInline = False
