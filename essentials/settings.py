import discord
import os
import dotenv
from dotenv import load_dotenv

from pollmaster.essentials.secrets import SECRETS


class Settings:
    def __init__(self):
        self.color = discord.Colour(int('7289da', 16))
        self.title_icon = "https://i.imgur.com/vtLsAl8.jpg" #PM
        self.author_icon = "https://i.imgur.com/TYbBtwB.jpg" #tag
        self.report_icon = "https://i.imgur.com/YksGRLN.png" #report
        self.owner_id = 117687652278468610
        self.msg_errors = False
        self.log_errors = True
        self.invite_link = \
            'https://discordapp.com/api/oauth2/authorize?client_id=444831720659877889&permissions=126016&scope=bot'

        self.load_secrets()

    def load_secrets(self):
        # secret
        load_dotenv()
        self.dbl_token = os.getenv('DBL_TOKEN')
        self.mongo_db = os.getenv('MONGO_DB')
        self.bot_token = os.getenv('BOT_TOKEN')
        self.mode = os.getenv('MODE')


SETTINGS = Settings()
