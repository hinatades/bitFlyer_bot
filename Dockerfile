FROM python:3.6.5-stretch

RUN mkdir -p /usr/src/app
RUN mkdir /log

WORKDIR /usr/src/app
COPY requirements.tet /usr/src/app
RUN pip install -r requirement.txt

COPY . /usr/src/app

RUN chmod 777 bot

EXPOSE 80

CMD ["uwsgi", "uwsgi.ini"]
