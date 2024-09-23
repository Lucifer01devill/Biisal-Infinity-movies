import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5207138613 6570247060 5533079371').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/talk_mrs_bot")
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/infinitymoviefiles')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002043045800 -1001866646571').split()]

#database 
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')


LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002051594756'))
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002215382811'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/f21404a4882698d5488dd.jpg')
START_IMG = environ.get('START_IMG', 'https://graph.org//file/505188b160b4d79a32269.jpg')
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1001964309084'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1001858701768'))
URL = environ.get('URL', 'happy-emilee-infinity-movies-hd-movies-hub01-7001d8e5.koyeb.app')
STICKERS_IDS = ('CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))

IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002043202934'))
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "28800"))


SHORTENER_API = environ.get("SHORTENER_API", "b2da06188bd355e103d16ab1b56db314709740df")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'tnshort.net')
SHORTENER_API2 = environ.get("SHORTENER_API2", "db8fd704394b5ab367448d70ed16f40cb5074b5f")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'gyanilinks.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "9bccb0b14ed6841652fa22d3481907788c1b8838")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'tnshort.net')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/links_tutorialbypp/25")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/links_tutorialbypp/27")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/links_tutorialbypp/25")

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi", "dual", "multi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 10
PREMIUM_POINT = 1000
auth_channel = environ.get('AUTH_CHANNEL', '-1001757701603')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001732232755'))
request_channel = environ.get('REQUEST_CHANNEL', '-1001821031247')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1002089150458'))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1001808193316')) #for channel post 

AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'tutorial2': TUTORIAL2,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'tutorial3': TUTORIAL3,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
    }
DEFAULT_POST_MODE = {
    'singel_post_mode' : True,
    'all_files_post_mode' : False
}
