FROM python:3
RUN pip install devpi-server devpi-web

RUN devpi-init

EXPOSE 3141

CMD devpi-server --host 0.0.0.0 