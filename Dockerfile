FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

COPY . /code/

WORKDIR /code/

RUN pip install -r requirements/dev.txt

CMD [ "python", "manage.py", "migrate" ]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]