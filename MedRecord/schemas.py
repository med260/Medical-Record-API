from pydantic import BaseModel, EmailStr


# ==============================
# Users
# ==============================
class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


# ==============================
# Patients
# ==============================
class PatientBase(BaseModel):
    name: str
    age: int


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


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True
    

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
