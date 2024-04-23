FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /ReferalApp
RUN apt-get update \
    && apt-get install -y libpq-dev python3-dev \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /ReferalApp/
RUN pip3 install --upgrade pip && pip install -r requirements.txt

COPY . /ReferalApp/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]