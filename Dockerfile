FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

WORKDIR /app

RUN pip3 install flask

COPY api.py /app

ENTRYPOINT [ "python3" ]

CMD [ "api.py" ]
