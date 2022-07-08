FROM python:3.7.6-buster
LABEL org.opencontainers.image.authors="moses_mbugua"

RUN mkdir /pythongitworkspace
COPY ./test-requirements.txt /pythongitworkspace/
COPY ./setup.py ./setup.py

RUN pip install --upgrade pip
RUN pip install -e .
RUN pip3 install -r /pythongitworkspace/test-requirements.txt

WORKDIR /pythongitworkspace

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true