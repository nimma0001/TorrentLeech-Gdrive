import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "1387711232:AAFImx_lJbd_q0Zbidwd_jxXoI07t62zr7Q"
    # The Telegram API things
    APP_ID = 1250468
    API_HASH = 5e52bbf5687e959215ba2a9463eee2ba
    OWNER_ID = 1111350430
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = [-1001153895452 1111350430 1219481510 691522795 -1001398749619]
    # the download location, where the 
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = 128
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = 
    # maximum message length in T
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = 6800
    EDIT_SLEEP_TIME_OUT = 15
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = 600
    MAX_TG_SPLIT_FILE_SIZE = 1072864000
    # add config vars for the dis
    FINISHED_PROGRESS_STR = "█"
    UN_FINISHED_PROGRESS_STR = "░"
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = "@VbOnTheWebTelEgram_"
#######
###
####
####leech@speedlestbot
    LEECH_COMMAND = "leech@speedlestbot"
    YTDL_COMMAND = "ytdl@speedlestbot"
    RCLONE_CONFIG = "type = drive
client_id = 472268816510-rtc4kmaeb4620fn0163pn2gjid2noohe.apps.googleusercontent.com
client_secret = zGz5xkWy-oKfsXrplvoAmkbL
scope = drive
token = {"access_token":"ya29.a0AfH6SMDyKvvDGv8qWxpOckzTaaEW4D9NIYfE0eR6pZj7vLZEZsFnm8-x9vNAgymuZuy8JQ86FKdmJnuyNfxXKRr-zeXsAExs33vV7kYKrSD02SC0aIVek7ycFSzIVf-RyW0BlBIaUeVzpncVFX3JBOZ45sPeK3soWD8","token_type":"Bearer","refresh_token":"1//0gT8JP3cD8fhmCgYIARAAGBASNwF-L9IraC6WmaP3cnkdg1Po-nJGYB27zClC7pjmYDz1j_QRZeV16qXwIyZINEx4Dxd__e7s1c0","expiry":"2020-07-08T16:05:55.049773068Z"}"
    DESTINATION_FOLDER = "Movie"
    GLEECH_COMMAND = "gleech@speedlestbot"
    INDEX_LINK = "https://folderdownload.freemovies.workers.dev/Exoticaz"
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status")
    SAVE_THUMBNAIL = "savethumbnail@speedlestbot"
    CLEAR_THUMBNAIL = "clearthumbnail@speedlestbot"
    UPLOAD_AS_DOC = "False"
    PYTDL_COMMAND_G = "pytdl@speedlestbot"
    LOG_COMMAND = "log"
    CLONE_COMMAND_G = "gclone@speedlestbot"
