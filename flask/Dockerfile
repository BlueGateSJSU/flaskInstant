FROM python:3

WORKDIR /flask
ADD requirements.txt /flask/requirements.txt

ADD init.sh /flask/init.sh
RUN ./init.sh
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
