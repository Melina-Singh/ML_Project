 FROM python:3.10.15-slim-buster

 WORKDIR /app

 COPY . /app

 RUN apt-get update -y && apt-get install -y awscli && apt-get clean

 RUN pip install -r requirements.txt

 COPY . .


 CMD["python3", "app.py"]

 EXPOSE 5000
