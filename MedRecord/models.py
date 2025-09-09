from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text , Boolean
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    role = Column(String, default="patient")
    records = relationship("MedicalRecord", back_populates="patient")
    is_active  = Column(Boolean, default=True)

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialization = Column(String)
    role = Column(String, default="doctor")
    records = relationship("MedicalRecord", back_populates="doctor")
    is_active  = Column(Boolean, default=True)
    years_of_experience = Column(Integer) 

class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    diagnosis = Column(Text, nullable=False)
    treatment = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    patient = relationship("Patient", back_populates="records")
    doctor = relationship("Doctor", back_populates="records")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active  = Column(Boolean , default=True)
    role = Column(String, nullable=False, default="user")
class Ailment(Base):
    __tablename__ = "ailments"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    description = Column(String)
    severity = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    patient = relationship("Patient", backref="ailments")

class Prescription(Base):
    __tablename__ = "prescriptions"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    medication_name = Column(String)
    dosage = Column(String)
    instructions = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    patient = relationship("Patient", backref="prescriptions")