from select import select
from sqlalchemy.orm import Session
import models, schemas


# ==============================
# Users
# ==============================
async def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump()) 
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user(db: Session, user_id: int):
    return await db.execute(
        select(models.User).where(models.User.id == user_id)
    ).scalar()


async def get_users(db: Session, skip: int = 0, limit: int = 10):
    return await db.execute(
        select(models.User).offset(skip).limit(limit)
    ).scalars().all()


async def delete_user(db: Session, user_id: int):
    user = await db.execute(
        select(models.User).where(models.User.id == user_id)
    )
    user = user.scalar()
    if user:
        await db.delete(user)
        await db.commit()
    return user


# ==============================
# Patients
# ==============================

async def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    await db.commit()
    await db.refresh(db_patient)
    return db_patient


async def get_patient(db: Session, patient_id: int):
    return await db.execute(
        select(models.Patient).where(models.Patient.id == patient_id)
    ).scalar()


async def get_patients(db: Session, skip: int = 0, limit: int = 10):
    return await db.execute(
        select(models.Patient).offset(skip).limit(limit)
    ).scalars().all()


async def delete_patient(db: Session, patient_id: int):
    patient = await db.execute(
        select(models.Patient).where(models.Patient.id == patient_id)
    )
    patient = patient.scalar()
    if patient:
        await db.delete(patient)
        await db.commit()
    return patient


# ==============================
# Ailments
# ==============================
async def create_ailment(db: Session, ailment: schemas.AilmentCreate, patient_id: int):
    db_ailment = models.Ailment(**ailment.model_dump(), patient_id=patient_id)
    db.add(db_ailment)
    await db.commit()
    await db.refresh(db_ailment)
    return db_ailment


async def get_ailments(db: Session, skip: int = 0, limit: int = 10):
    return await db.execute(
        select(models.Ailment).offset(skip).limit(limit)
    ).scalars().all()


async def get_patient_ailments(db: Session, patient_id: int):
    return await db.execute(
        select(models.Ailment).where(models.Ailment.patient_id == patient_id)
    ).scalars().all()


async def delete_ailment(db: Session, ailment_id: int):
    ailment = await db.execute(
        select(models.Ailment).where(models.Ailment.id == ailment_id)
    )
    ailment = ailment.scalar()
    if ailment:
        await db.delete(ailment)
        await db.commit()
    return ailment


# ==============================
# Prescriptions
# ==============================
async def create_prescription(db: Session, prescription: schemas.PrescriptionCreate, patient_id: int):
    db_prescription = models.Prescription(**prescription.model_dump(), patient_id=patient_id)
    db.add(db_prescription)
    await db.commit()
    await db.refresh(db_prescription)
    return db_prescription


async def get_prescriptions(db: Session, skip: int = 0, limit: int = 10):
    return await db.execute(
        select(models.Prescription).offset(skip).limit(limit)
    ).scalars().all()


async def delete_prescription(db: Session, prescription_id: int):
    prescription = await db.execute(
        select(models.Prescription).where(models.Prescription.id == prescription_id)
    )
    prescription = prescription.scalar()
    if prescription:
        await db.delete(prescription)
        await db.commit()
    return prescription


# ==============================
# Doctors
# ==============================
async def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.model_dump())
    db.add(db_doctor)
    await db.commit()
    await db.refresh(db_doctor)
    return db_doctor


async def get_doctor(db: Session, doctor_id: int):
    return await db.execute(
        select(models.Doctor).where(models.Doctor.id == doctor_id)
    ).scalar()


async def get_doctors(db: Session, skip: int = 0, limit: int = 10):
    return await db.execute(
        select(models.Doctor).offset(skip).limit(limit)
    ).scalars().all()


async def assign_doctor_to_patient(db: Session, doctor_id: int, patient_id: int):
    patient = await db.execute(
        select(models.Patient).where(models.Patient.id == patient_id)
    )
    patient = patient.scalar()
    if patient:
        patient.doctor_id = doctor_id
        await db.commit()
        await db.refresh(patient)
    return patient


async def get_doctor_patients(db: Session, doctor_id: int):
    return await db.execute(
        select(models.Patient).where(models.Patient.doctor_id == doctor_id)
    ).scalars().all()


async def deactivate(db: Session, user_id: int):
    user = await db.execute(
        select(models.User).where(models.User.id == user_id)
    )
    user = user.scalar()
    if user:
        user.is_active = False
        await db.commit()
        await db.refresh(user)
    return user