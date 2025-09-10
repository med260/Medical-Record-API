
# MedRec API

FastAPI backend for medical records with JWT authentication.

## 🚀 Features
- JWT auth (Doctor/Patient roles)  
- Doctors & Patients CRUD (list, get)  
- PostgreSQL + Async SQLAlchemy  
- Swagger UI at `/docs`  

## 🛠️ Tech
FastAPI · PostgreSQL · SQLAlchemy (Async) · JWT · Docker  

## 📦 Installation
```
git clone https://github.com/med260/Medical-Record-API.git
cd Medical-Record-API
python -m venv venv && source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
uvicorn app.main:app --reload
````

## 📚 API Docs

* Swagger → [http://localhost:8000/docs](http://localhost:8000/docs)

## 🔐 Auth

* `POST /login` – Login
* `POST /register` – Register
* 
## 👨‍⚕️ Doctors

* `GET /doctors` – List
* `GET /doctors/{id}` – Detail

## 👤 Patients

* `GET /patients` – List
* `GET /patients/{id}` – Detail

## 🐳 Docker

```bash
docker-compose up -d
```

