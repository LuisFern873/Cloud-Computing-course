FROM python:3.11.3-alpine
RUN apk update && apk add --no-cache gcc
RUN apk add --no-cache python3-dev mariadb-connector-c-dev build-base
WORKDIR /api_tareas
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /api_tareas
EXPOSE 5003
CMD flask run --host=0.0.0.0 --port=5003