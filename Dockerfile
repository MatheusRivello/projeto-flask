FROM python:3

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip && pip install flask

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD [ "python", "app.py" ]
