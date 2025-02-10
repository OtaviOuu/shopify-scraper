FROM python:3.10-slim

WORKDIR /app

COPY src/ /app/src
COPY templates/ /app/templates
COPY README.md /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

ENV PYTHONPATH=/app/src
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "5000"]

