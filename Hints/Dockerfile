FROM python:3.12-slim
COPY requirements .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
COPY . .
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]