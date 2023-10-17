RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN apt install ffmpeg -y

WORKDIR /root/userbot

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
RUN brew install redis
CMD ["python3","main.py"]
