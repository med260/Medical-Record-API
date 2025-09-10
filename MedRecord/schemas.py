from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime

# ==============================
# Roles Enum
# ==============================
class RoleEnum(str, Enum):
    doctor = "doctor"
    admin = "admin"
    patient = "patient"

# ==============================
# Gender Enum
# ==============================
class GenderEnum(str, Enum):
    male = "male"
    female = "female"

# ==============================
# Base User Schema
# ==============================
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: RoleEnum = RoleEnum.patient

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# ==============================
# Patient Schema
# ==============================
class PatientBase(UserBase):
    name: str
    age: int
    gender: GenderEnum

class PatientCreate(PatientBase):
    password: str
    doctor_id: Optional[int] = None

class PatientResponse(PatientBase):
    id: int
    is_active: Optional[bool] = True
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# ==============================
# Doctor Schema
# ==============================
class DoctorBase(BaseModel):
    username: str
    email: str
    name: str          
    specialization: str
    years_of_experience: int

class DoctorCreate(DoctorBase):
    password: str

class DoctorResponse(DoctorBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ==============================
# Medical Record Schema
# ==============================

class MedicalRecordBase(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: str
    treatment: str | None = None

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecordResponse(MedicalRecordBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# ==============================
# Token Schema
# ==============================
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None

class TokenData(BaseModel):
    username: Optional[str] = None

# ==============================
# Login Schema
# ==============================
class UserLogin(BaseModel):
    email: EmailStr
    password: str