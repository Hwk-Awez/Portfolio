FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG HUGGINGFACE_API_TOKEN
ENV HUGGINGFACE_API_TOKEN=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

RUN python ron/ingest.py
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000", "--config", "gunicorn.conf.py"]