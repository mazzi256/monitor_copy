FROM python:3
ENV PYTHONUNBUFFRED 1
RUN mkdir /api
COPY . /api/
RUN pip freeze > requirements.txt