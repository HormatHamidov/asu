FROM python:3.10.1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN apt-get update && apt-get install -y netcat
RUN pip install -r requirements.txt
COPY . /code/

ENTRYPOINT ["/code/scripts/entrypoint.sh"]