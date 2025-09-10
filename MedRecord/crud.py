from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models, schemas

# ==============================
# Users
# ==============================
async def deactivate_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalar()
    if user:
        user.is_active = False
        await db.commit()
        await db.refresh(user)
    return user
# ==============================
# Patients
# ==============================
async def create_patient(db: AsyncSession, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.model_dump(exclude={"password"}))
    # Hash password and set
    db_patient.hashed_password = models.pwd_context.hash(patient.password)
    db.add(db_patient)
    await db.commit()
    await db.refresh(db_patient)
    return db_patient

async def get_patient(db: AsyncSession, patient_id: int):
    result = await db.execute(select(models.Patient).where(models.Patient.id == patient_id))
    return result.scalar()

async def get_patients(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Patient).offset(skip).limit(limit))
    return result.scalars().all()

async def delete_patient(db: AsyncSession, patient_id: int):
    patient = await get_patient(db, patient_id)
    if patient:
        await db.delete(patient)
        await db.commit()
    return patient

# ==============================
# Doctors
# ==============================
async def create_doctor(db: AsyncSession, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.model_dump(exclude={"password"}))
    db_doctor.hashed_password = models.get_password_hash(doctor.password)
    db.add(db_doctor)
    await db.commit()
    await db.refresh(db_doctor)
    return db_doctor

async def get_doctor(db: AsyncSession, doctor_id: int):
    result = await db.execute(select(models.Doctor).where(models.Doctor.id == doctor_id))
    return result.scalar()

async def get_doctors(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Doctor).offset(skip).limit(limit))
    return result.scalars().all()

async def assign_doctor_to_patient(db: AsyncSession, doctor_id: int, patient_id: int):
    patient = await get_patient(db, patient_id)
    if patient:
        patient.doctor_id = doctor_id
        await db.commit()
        await db.refresh(patient)
    return patient

async def get_doctor_patients(db: AsyncSession, doctor_id: int):
    result = await db.execute(select(models.Patient).where(models.Patient.doctor_id == doctor_id))
    return result.scalars().all()


# ==============================
# Medical Records
# ==============================

async def create_medical_record(db: AsyncSession, record: schemas.MedicalRecordCreate):
    db_record = models.MedicalRecord(**record.model_dump())
    db.add(db_record)
    await db.commit()
    await db.refresh(db_record)
    return db_record

async def get_medical_record(db: AsyncSession, record_id: int):
    result = await db.execute(select(models.MedicalRecord).where(models.MedicalRecord.id == record_id))
    return result.scalar()

async def get_medical_records(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.MedicalRecord).offset(skip).limit(limit))
    return result.scalars().all()

async def update_medical_record(db: AsyncSession, record_id: int, updated_data: schemas.MedicalRecordCreate):
    result = await db.execute(select(models.MedicalRecord).where(models.MedicalRecord.id == record_id))
    record = result.scalar()
    if not record:
        return None
    for key, value in updated_data.model_dump().items():
        setattr(record, key, value)
    await db.commit()
    await db.refresh(record)
    return record

async def delete_medical_record(db: AsyncSession, record_id: int):
    result = await db.execute(select(models.MedicalRecord).where(models.MedicalRecord.id == record_id))
    record = result.scalar()
    if not record:
        return None
    await db.delete(record)
    await db.commit()
    return record
