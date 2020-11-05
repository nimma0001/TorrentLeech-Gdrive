FROM ubuntu:20.04


RUN mkdir ./app
RUN chmod 777 ./app
WORKDIR /app

RUN apt -qq update

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata
ENV AUTH_CHANNEL="-1001153895452"
ENV API_HASH="5e52bbf5687e959215ba2a9463eee2ba"
ENV APP_ID=1250468
ENV TG_BOT_TOKEN="1387711232:AAFImx_lJbd_q0Zbidwd_jxXoI07t62zr7Q"
ENV LEECH_COMMAND="leech@speedlestbot"
ENV YTDL_COMMAND="ytdl@speedlestbot
ENV GLEECH_COMMAND="gleech@speedlestbot"
ENV TELEGRAM_LEECH_COMMAND_G="tleech@speedlestbot"
ENV PYTDL_COMMAND_G="pytdl@speedlestbot"
ENV CLONE_COMMAND_G="clone@speedlestbot"
ENV UPLOAD_AS_DOC=true
ENV INDEX_LINK="https://folderdownload.freemovies.workers.dev/Movie"
ENV SAVE_THUMBNAIL="savethumbnail@speedlestbot"
ENV CLEAR_THUMBNAIL="clearthumbnail@speedlestbot"

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
