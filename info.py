import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'DPX')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['22404062'])
API_HASH = environ['162d4eb8c9cbfe558121c6cf41f8df43']
BOT_TOKEN = environ['6328374317:AAHkCzq47FK252GeJ_Uf1HNxRut24GPKpoI']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['1165215979'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['deplix_zone'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('1165215979', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('deplix_zoneL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['mongodb+srv://Anuwa:Anuwa@cluster0.qsvet.mongodb.net/?retryWrites=true&w=majority']
DATABASE_NAME = environ['Project 0']
COLLECTION_NAME = environ.get('DPX', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('HI WELCOME', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
