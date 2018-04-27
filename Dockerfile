FROM python:2.7-slim

WORKDIR /app

Add . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME cloudworld

CMD python  app.py forecast.html
