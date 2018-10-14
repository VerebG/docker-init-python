FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/build

RUN apt-get update && \
    apt-get -qq install python3.6 python3-pip dumb-init && \
    /usr/bin/pip3 install pyinstaller

VOLUME /build

COPY src /build/src
COPY build/docker_init.sh /init.sh
COPY requirements.txt /build/requirements.txt
COPY VERSION /VERSION

RUN chmod 777 /init.sh

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["/init.sh"]