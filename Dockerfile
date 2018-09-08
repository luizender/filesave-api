FROM alpine:3.8
MAINTAINER Luiz Gustavo Ender <luiz.ender@gmail.com>
ENV CLOUD_SDK_VERSION 215.0.0
ENV PATH /google-cloud-sdk/bin:$PATH
RUN apk add --no-cache --update python3 python3-dev make gcc musl-dev curl && \
    curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    ln -s /lib /lib64
WORKDIR /code
COPY . /code/
RUN pip3 install -r requirements.txt --no-cache-dir
CMD [ "make", "run" ]