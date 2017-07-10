FROM alpine:3.4

MAINTAINER NHS Digital Delivery Centre, CIS Team. Email: HSCIC.DL-CIS@nhs.net

# Install python 3 basics
RUN apk update && \
    apk add ca-certificates && \
    apk add python3 && \
    apk add python3-dev build-base libffi-dev openssl-dev --update-cache && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -rf /usr/lib/python*/ensurepip && \
    rm -rf /root/.cache && \
    rm -rf /var/cache/apk/*

# Create unprivileged user
RUN adduser -S service

MAINTAINER NHS Digital Delivery Centre, CIS Team. Email: HSCIC.DL-CIS@nhs.net

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt
