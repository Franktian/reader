FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /legacy
WORKDIR /legacy

ADD requirements.txt /legacy

RUN pip install -r requirements.txt

ADD . /legacy

ADD ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 8000 5432

ENTRYPOINT [ "/entrypoint.sh" ]
