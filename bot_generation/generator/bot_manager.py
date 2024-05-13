from besser.bot.core.bot import Bot
from besser.bot.platforms.websocket import WEBSOCKET_PORT


class BotManager:
    port = 8765

    def __init__(self):
        self.bots: dict = {}

    def add_bot(self, bot: Bot):
        if bot.name in self.bots:
            raise ValueError(f"Bot with name {bot.name} already exists")
        bot.set_property(WEBSOCKET_PORT, BotManager.port)
        BotManager.port += 1
        self.bots[bot.name] = bot

