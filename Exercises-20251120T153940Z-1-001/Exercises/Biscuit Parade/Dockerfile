FROM python:3.11-slim

WORKDIR /app

COPY webapp/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY webapp/ .

ENV FLASK_APP=app
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
