FROM python:3.8-slim-buster


ENTRYPOINT [ "/bin/bash" ]
WORKDIR /home/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /home/app/


