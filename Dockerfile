FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flake8 

EXPOSE 5000

CMD ["python", "app.py"]

