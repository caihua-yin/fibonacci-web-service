# Dockerfile for fibonacci-web-service
FROM debian:jessie
MAINTAINER Caihua Yin <alend.yin@gmail.com>

RUN apt-get update && \
    apt-get install -y python build-essential python-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY tornado-4.2.1.tar.gz /opt/fibonacci-web-service/
RUN cd /opt/fibonacci-web-service/ && \
    tar xvzf tornado-4.2.1.tar.gz && \
    cd tornado-4.2.1 && \
    python setup.py build && \
    python setup.py install

COPY lib/fibonacci.py /opt/fibonacci-web-service/lib/
COPY bin/fibonacci_web_service.py /opt/fibonacci-web-service/bin/

WORKDIR /opt/fibonacci-web-service/bin/
ENTRYPOINT ["/opt/fibonacci-web-service/bin/fibonacci_web_service.py"]

EXPOSE 8888
