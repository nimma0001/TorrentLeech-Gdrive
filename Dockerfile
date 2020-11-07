FROM ubuntu:20.04


RUN mkdir ./app
RUN chmod 777 ./app
WORKDIR /app

RUN apt -qq update

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata
ENV AUTH_CHANNEL="-1001153895452 754658818 691522795"
#ENV API_HASH="5e52bbf5687e959215ba2a9463eee2ba"
#ENV APP_ID=1250468
ENV API_HASH="b7b0949f6eefb3927c20c1684dff4958"
ENV APP_ID=1138546
ENV TG_BOT_TOKEN="1364169619:AAFhXKBpVHCHI5aNZICefFAC5HCffNmLhaM"
#ENV TG_BOT_TOKEN="1387711232:AAFImx_lJbd_q0Zbidwd_jxXoI07t62zr7Q"
ENV LEECH_COMMAND="leech@speedlestbot"
ENV YTDL_COMMAND="ytdl@speedlestbot"
ENV GLEECH_COMMAND="gleech@speedlestbot"
ENV TELEGRAM_LEECH_COMMAND_G="tleech@speedlestbot"
ENV PYTDL_COMMAND_G="pytdl@speedlestbot"
ENV CLONE_COMMAND_G="clone@speedlestbot"
ENV UPLOAD_AS_DOC=true
ENV INDEX_LINK="https://folderdownload.freemovies.workers.dev/Movie"
ENV SAVE_THUMBNAIL="savethumbnail@speedlestbot"
ENV CLEAR_THUMBNAIL="clearthumbnail@speedlestbot"
ENV OWNER_ID="1111350430"
#ENV DESTINATION_FOLDER=Movie
ENV CUSTOM_FILE_NAME=" @VbOnTheWeBTeleGram "
#ENV RCLONE_CONFIG="type = drive\nclient_id = 472268816510-rtc4kmaeb4620fn0163pn2gjid2noohe.apps.googleusercontent.com\nclient_secret = zGz5xkWy-oKfsXrplvoAmkbL\nscope = drive\ntoken = {"access_token":"ya29.A0AfH6SMBMeCOCM1u8KzqXMsF7_5PRP4bxPfwx6pbWBP-sk3d8T23pnkZGlDXvjlYNuedQT3KLoh3ZInqlwsmmgb-D_ZBFBxiU1WkAGzDeKywr5yJs0oJ9dRgSwkJwS4tSX-42ZHBe7njZdGoKH5bpUDYc2DmLT9e2KgypPe7ipYmEAQ","token_type":"Bearer","refresh_token":"1//0gT8JP3cD8fhmCgYIARAAGBASNwF-L9IraC6WmaP3cnkdg1Po-nJGYB27zClC7pjmYDz1j_QRZeV16qXwIyZINEx4Dxd__e7s1c0","expiry":"2020-10-23T10:34:50.284204302+05:30"}"

RUN apt -qq install -y git aria2 wget curl busybox unzip unrar tar python3 ffmpeg python3-pip
RUN wget https://rclone.org/install.sh
RUN bash install.sh

RUN mkdir /app/gautam
RUN wget -O /app/gautam/gclone.gz https://git.io/JJMSG
RUN gzip -d /app/gautam/gclone.gz
RUN chmod 0775 /app/gautam/gclone

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash","start.sh"]
