FROM python:stretch

COPY . /usr/app
WORKDIR /usr/app

RUN pip install -r requirements.txt

ENTRYPOINT [ "gunicorn", "-b", ":8080", "main:APP" ]