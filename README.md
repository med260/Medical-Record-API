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
**Project Structure**
```
MedRecord/
├── app/
│   ├── __pycache__/          # Python cache (ignored)
│   ├── DB/                   # Database related files
│   ├── routes/               # API route handlers
│   ├── config.py             # Configuration settings
│   ├── crud.py               # Database operations
│   ├── data.py               # Data utilities
│   ├── database.py           # Database connection
│   ├── main.py               # FastAPI application
│   ├── models.py             # SQLAlchemy models
│   └── schemas.py            # Pydantic schemas
├── .env                      # Environment variables (ignored)
├── docker-compose.yml        # Multi-container setup
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

**Key Files:**
- `main.py` - FastAPI app entry point
- `models.py` - Database table definitions
- `schemas.py` - Request/response models
- `crud.py` - Create, Read, Update, Delete operations
- `database.py` - Database connection setup
- `docker-compose.yml` - Docker configuration
- `requirements.txt` - Python dependencies

**Note:** `__pycache__/` and `.env` are excluded from version control via `.gitignore`
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
- **ReDoc**: `http://localhost:8000/redoc`

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
