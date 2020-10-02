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
ENV TG_BOT_TOKEN="1164102016:AAGozPKR8BdW2q6uJfb6yOIXR0RsoXUOjh8"

RUN apt -qq install -y git aria2 wget curl busybox unzip unrar tar python3 ffmpeg python3-pip

RUN mkdir /app/gautam

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash","start.sh"]
