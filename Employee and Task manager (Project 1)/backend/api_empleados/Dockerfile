FROM python:3.11.3-alpine
RUN apk update && apk add --no-cache gcc
RUN apk add --no-cache python3-dev mariadb-connector-c-dev build-base
WORKDIR /api_empleados
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /api_empleados
EXPOSE 5002
CMD flask run --host=0.0.0.0 --port=5002