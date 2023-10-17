RUN apt-get install redis-server
COPY . /app
WORKDIR /app
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD ["python3","main.py"]
