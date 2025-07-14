# Assignment: Python API Development for KPA

This repository contains a simple and robust REST API built using **Python** for the **KPA (Key Performance Appraisal)** system. The API is containerized with Docker, and designed for easy testing, deployment, and future extension.

---

##  Project Structure

```

.
├── app/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   └── services/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

````

> If using FastAPI, the folder may also include `schemas/`, `database.py`, and more.

---

##  Tech Stack

- **Backend**: Python (FastAPI / Flask)
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose
- **ORM**: SQLAlchemy or Tortoise ORM (if applicable)

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/RohanDobriyal/Assignment-Python----API-dev-for-KPA-.git
cd Assignment-Python----API-dev-for-KPA-
````

### 2. Run Locally (Without Docker)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload   # If using FastAPI
```

> Local API will run at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

##  Running with Docker

### Build & Run

```bash
docker-compose up --build
```

### Stop Containers

```bash
docker-compose down
```

---

##  Sample Endpoints (Example for FastAPI)

* `POST /api/signup` – User registration
* `POST /api/login` – Login using phone number and password
* `GET /api/user/{id}` – Get user details
* `POST /api/kpa-form` – Submit KPA form
* `GET /api/kpa-form/{id}` – Retrieve KPA form by ID

> Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

##  Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

##  docker-compose.yml

```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: kpa_db
    ports:
      - "5432:5432"
```

---

##  Features Implemented

* [x] Signup & Login (with validation)
* [x] KPA Form submission & retrieval
* [x] RESTful API structure with modular code
* [x] Dockerized for local and cloud deployment
* [x] Swagger/OpenAPI docs auto-generated

---

##  Author

* [Rohan Dobriyal](https://github.com/RohanDobriyal)

---



