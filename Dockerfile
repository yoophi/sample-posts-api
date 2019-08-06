FROM python:3.7.4-alpine

ENV FLASK_APP application.py
ENV FLASK_CONFIG production

RUN adduser -D webapp
USER webapp

WORKDIR /home/webapp

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY application.py boot.sh ./

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
