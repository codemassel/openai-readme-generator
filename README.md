# AI-powered README Generator ![Python](https://img.shields.io/badge/python-3.11-blue) ![OpenAI](https://img.shields.io/badge/OpenAI-API-red) ![Docker](https://img.shields.io/badge/docker-ready-lightgrey)
Generiert automatisch komplette READMEs für GitHub-Repositories mit OpenAI / GPT-3.5 API.

Unterstützt sowohl **DummyAI** (kostenlos) als auch **OpenAI API**.
Mit **lokalem Cache**, **Docker-Setup** und **FastAPI Webservice**.

---

## Features

* Generiert ein komplettes README für jedes GitHub-Repo
* Lokaler Cache verhindert wiederholte API-Requests
* DummyAI für Entwicklung ohne OpenAI-Quota
* Einfacher Wechsel zu OpenAI für echte README-Generierung
* Dockerized FastAPI-Server für lokale Tests oder Cloud-Deployment

---

## Installation

1. Repository klonen:

```bash
git clone https://github.com/Codemassel/openai-readme-generator.git
cd openai-readme-generator
```

2. Virtuelle Umgebung erstellen (optional, lokal):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

4. `.env` Datei erstellen (nicht ins Repo hochladen!):

```
OPENAI_API_KEY=dein_openai_key
```

* DummyAI funktioniert natürlich auch ohne `.env`.

---

## CLI Nutzung (lokal)

```bash
python app/main.py
```

* Beachte die Inputs für das auszulesende Repo:

  * GitHub Owner
  * Repo Name
* Ausgabe: `GENERATED_README.md` im Projektordner

---

## FastAPI Webservice

1. Docker Image bauen:

```bash
docker build -t readme-generator .
```

2. Container starten:

```bash
docker run -p 8000:8000 -v ${PWD}/app:/app readme-generator
```

* Zugriff: `http://localhost:8000/docs` (Swagger UI)
* POST `/generate-readme` mit Body:

```json
{
  "owner": "EingegebenerOwner",
  "repo_name": "EingegebensRepo"
}
```

* Antwort: generiertes README

---

## DummyAI vs. OpenAI

* **DummyAI:** Kostenlos, schnell, für Tests und Entwicklung
* **OpenAI:** Nutzt GPT-3.5 oder GPT-4, echtes AI-Generated README
* Umschalten in `app/main.py` oder `app/api.py`:

```python
USE_DUMMY = True  # DummyAI
USE_DUMMY = False # OpenAI API
```

---

## Lokaler Cache

* `cache.json` speichert bereits generierte READMEs
* Verhindert wiederholte API-Requests
* Nicht ins Repo hochladen (`.gitignore`)

---

## Docker-Setup

* Exposed Port: 8000 (lokal) oder anpassen wie gewünscht
* Hot-Reload (für Entwicklung):

```dockerfile
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

* Volumes für Hot-Reload:

```bash
docker run -p 8000:8000 -v ${PWD}/app:/app openai-readme-generator
```

---

## Projektstruktur

```
openai-readme-generator/
├── app/
│   ├── main.py
│   ├── api.py
│   ├── ai_generator.py
│   ├── dummy_ai.py
│   ├── readme_builder.py
│   ├── github_client.py
│   ├── utils.py
│   ├── cache_manager.py
│   └── logging_config.py
├── requirements.txt
├── Dockerfile
├── cache.json (ignored)
└── .gitignore
```

---

## .gitignore

```
.env
cache.json
venv/
__pycache__/
*.pyc
```

* Verhindert, dass sensible Daten hochgeladen werden

---

## Zukunft / Erweiterungen

* OpenAI API Key Management in Cloud Secrets
* Remote Deployment (Railway, Render, AWS)
* Weitere AI-Tools integrieren
