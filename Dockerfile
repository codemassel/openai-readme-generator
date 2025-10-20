# 1️⃣ Base Image
FROM python:3.11-slim

# 2️⃣ Arbeitsverzeichnis
WORKDIR /app

# 3️⃣ Kopiere Code + requirements
COPY ./app /app
COPY requirements.txt /app

# 4️⃣ Abhängigkeiten installieren
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Port exposed
EXPOSE 8000

# 6️⃣ Startbefehl
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
