# MedRec API

FastAPI backend for medical records management with JWT authentication.

## 🚀 Features

- **Auth**: JWT security with Doctor/Patient roles
- **CRUD**: Patients, Doctors, Ailments, Prescriptions
- **DB**: PostgreSQL with Async SQLAlchemy
- **Docs**: Auto-generated Swagger at `/docs`

## 🛠️ Tech

- FastAPI
- PostgreSQL
- SQLAlchemy (Async)
- JWT
- Docker

## 📁 Structure

```
MedRec/
├── app/
│   ├── main.py          # App entry
│   ├── database.py      # DB connection
│   ├── models.py        # DB models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # CRUD operations
│   └── routes.py        # API routes
├── requirements.txt
└── Dockerfile
```

## 🏃‍♂️ Quick Start

```bash
# 1. Setup
python -m venv MedRec
source MedRec/bin/activate  # or `MedRec\Scripts\activate` on Windows

# 2. Install
pip install -r requirements.txt

# 3. Run
uvicorn app.main:app --reload
```

## 📚 API Docs

- **Swagger UI**: `http://localhost:8000/docs`

## 🔐 Auth Endpoints

- `POST /login` - Login
- `POST /register` - Register
- `GET /users/me` - User profile

## 👨‍⚕️ Doctor Endpoints

- `GET /doctors` - List doctors
- `POST /doctors` - Create doctor
- `GET /doctors/{id}` - Get doctor

## 👤 Patient Endpoints

- `GET /patients` - List patients
- `POST /patients` - Create patient
- `GET /patients/{id}` - Get patient

## 🐳 Docker

```bash
docker-compose up -d
```
