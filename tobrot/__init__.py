#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52

import os
import time
import logging

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
   from tobrot.sample_config import Config
from logging.handlers import RotatingFileHandler

# TODO: is there a better way?
TG_BOT_TOKEN = "1387711232:AAFImx_lJbd_q0Zbidwd_jxXoI07t62zr7Q"
APP_ID = "1250468"
API_HASH = "5e52bbf5687e959215ba2a9463eee2ba"
OWNER_ID = "1111350430"
AUTH_CHANNEL = "-1001153895452"
DOWNLOAD_LOCATION = "./DOWNLOADS"
DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 15))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "TorrentLeech-Gdrive")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail")
    UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "False")
    PYTDL_COMMAND_G = os.environ.get("PYTDL_COMMAND_G", "pytdl")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log")
    CLONE_COMMAND_G = os.environ.get("CLONE_COMMAND_G", "gclone")

if os.path.exists("TorrentLeech-Gdrive.txt"):
	with open("Torrentleech-Gdrive.txt", "r+") as f_d:
		f_d.truncate(0)

# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "Torrentleech-Gdrive.txt",
            maxBytes=FREE_USER_MAX_FILE_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
