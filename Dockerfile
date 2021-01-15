FROM python:3

RUN apt-get -y update
RUN pip3 install flask
RUN apt-get install apache2 -y
RUN apt-get install libapache2-mod-wsgi -y

WORKDIR /usr/src/app
COPY . .

EXPOSE 5000
CMD ["python3", "./app.py"]