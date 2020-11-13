FROM python:3.8

WORKDIR /tmp

COPY app.py /tmp
COPY requirements.txt /tmp
COPY gunicorn_config.py /tmp
COPY cache_test.py /tmp
COPY wsgi.py /tmp

RUN ls -lah /tmp
RUN pip install -r "/tmp/requirements.txt"

EXPOSE 8000

ENV FLASK_APP = /tmp/f2.py
ENV SERVER_NAME = '0.0.0.0'

CMD ["gunicorn", "--config", "gunicorn_config.py", "app:app"]

# $ docker build -t t1 . && docker run -p 8000:8000 t1:latest