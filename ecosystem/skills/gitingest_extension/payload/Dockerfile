FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ['gunicorn', '-b', '0.0.0.0:5000', '--workers', '3', 'app:app']