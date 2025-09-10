from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from config import settings

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ==============================
# User Base
# ==============================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="user")  # doctor, patient, admin
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # ------------------------------
    # Authentication Methods
    # ------------------------------
    def authenticate(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)

    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)

    def create_jwt(self, expires_delta: timedelta = None):
        to_encode = {"sub": str(self.id), "role": self.role}
        expire = datetime.now() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

# ==============================
# Doctor
# ==============================
class Doctor(User):
    __tablename__ = "doctors"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    name = Column(String, nullable=False)
    specialization = Column(String)
    years_of_experience = Column(Integer)
    records = relationship("MedicalRecord", back_populates="doctor")

# ==============================
# Patient
# ==============================
class Patient(User):
    __tablename__ = "patients"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    records = relationship("MedicalRecord", back_populates="patient")
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    def __init__(self, **kwargs):
        kwargs['role'] = 'patient'  # Force role to 'patient'
        super().__init__(**kwargs)
# ==============================
# Medical Record
# ==============================
class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    diagnosis = Column(Text, nullable=False)
    treatment = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    patient = relationship("Patient", back_populates="records")
    doctor = relationship("Doctor", back_populates="records")
# ==============================