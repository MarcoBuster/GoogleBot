class MessageUpdate:
    def __init__(self, user, bot, chat, message):
        self.bot = bot
        self.user = user
        self.chat = chat
        self.message = message
