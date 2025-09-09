from enum import Enum
from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel,EmailStr , field_validator

# ==============================
# Roles Enum
# ==============================
class RoleEnum(str, Enum):
    doctor = "doctor"
    admin = "admin"
    user = "user"
    patient = "patient"

# ==============================
# gender Enum
# ==============================
class genderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"
# ==============================
# Users
# ==============================

class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True
class UserCreate(BaseModel):  # 
    username: str
    email: EmailStr
    password: str
    role: Optional[RoleEnum] = RoleEnum.user

    @field_validator("role")
    @classmethod
    def validate_role(cls, value):
        allowed = [e.value for e in RoleEnum]
        if value not in allowed:
            raise ValueError(f"Invalid role '{value}'. Allowed: {', '.join(allowed)}")
        return value

class UserResponse(BaseModel):  # ← For OUTPUT responses
    id: int
    username: str
    email: str
    role: str  # User role (e.g., "admin", "user")
    is_active: bool


# ==============================
# Patients
# ==============================
class PatientBase(BaseModel):
    name: str
    age: int
    gender: genderEnum

class PatientCreate(PatientBase):
    doctor_id: int | None = None


class PatientResponse(PatientBase):
    id: int
    doctor_id: int | None = None

    class Config:
        from_attributes = True


# ==============================
# Ailments
# ==============================
class AilmentBase(BaseModel):
    description: str
    severity: str


class AilmentCreate(AilmentBase):
    pass


class AilmentResponse(AilmentBase):
    id: int
    patient_id: int

    class Config:
        from_attributes = True


# ==============================
# Prescriptions
# ==============================
class PrescriptionBase(BaseModel):
    medication_name: str
    dosage: str
    instructions: str


class PrescriptionCreate(PrescriptionBase):
    pass


class PrescriptionResponse(PrescriptionBase):
    id: int
    patient_id: int

    class Config:
        from_attributes = True


# ==============================
# Doctors
# ==============================
class DoctorBase(BaseModel):
    name: str
    specialization: str
    years_of_experience: int
    role: RoleEnum = RoleEnum.doctor

class DoctorCreate(DoctorBase):
    pass




class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True
    
