RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN apt install ffmpeg -y

WORKDIR /root/userbot

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3","main.py"]
