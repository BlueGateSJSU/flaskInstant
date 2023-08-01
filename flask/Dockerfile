FROM python:3

WORKDIR /flask
ADD requirements.txt /flask/requirements.txt

ADD init.sh /flask/init.sh
RUN apt-get -y update 
RUN apt-get -y install cmake libgl1-mesa-glx libglib2.0-0

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
