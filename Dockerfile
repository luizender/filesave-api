FROM alpine:3.8
MAINTAINER Luiz Gustavo Ender <luiz.ender@gmail.com>
RUN apk add --no-cache --update python3 python3-dev make gcc musl-dev
WORKDIR /code
COPY . /code/
RUN pip3 install -r requirements.txt --no-cache-dir
CMD [ "make", "run" ]