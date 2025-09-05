from sqlalchemy.orm import Session
import models, schemas


# ==============================
# Users
# ==============================
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


# ==============================
# Patients
# ==============================
def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()


def get_patients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Patient).offset(skip).limit(limit).all()


def delete_patient(db: Session, patient_id: int):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient:
        db.delete(patient)
        db.commit()
    return patient


# ==============================
# Ailments
# ==============================
def create_ailment(db: Session, ailment: schemas.AilmentCreate, patient_id: int):
    db_ailment = models.Ailment(**ailment.model_dump(), patient_id=patient_id)
    db.add(db_ailment)
    db.commit()
    db.refresh(db_ailment)
    return db_ailment


def get_ailments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Ailment).offset(skip).limit(limit).all()


def get_patient_ailments(db: Session, patient_id: int):
    return db.query(models.Ailment).filter(models.Ailment.patient_id == patient_id).all()


def delete_ailment(db: Session, ailment_id: int):
    ailment = db.query(models.Ailment).filter(models.Ailment.id == ailment_id).first()
    if ailment:
        db.delete(ailment)
        db.commit()
    return ailment


# ==============================
# Prescriptions
# ==============================
def create_prescription(db: Session, prescription: schemas.PrescriptionCreate, patient_id: int):
    db_prescription = models.Prescription(**prescription.model_dump(), patient_id=patient_id)
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription


def get_prescriptions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Prescription).offset(skip).limit(limit).all()


def delete_prescription(db: Session, prescription_id: int):
    prescription = db.query(models.Prescription).filter(models.Prescription.id == prescription_id).first()
    if prescription:
        db.delete(prescription)
        db.commit()
    return prescription


# ==============================
# Doctors
# ==============================
def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.model_dump())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()


def get_doctors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Doctor).offset(skip).limit(limit).all()


def assign_doctor_to_patient(db: Session, doctor_id: int, patient_id: int):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient:
        patient.doctor_id = doctor_id
        db.commit()
        db.refresh(patient)
    return patient


def get_doctor_patients(db: Session, doctor_id: int):
    return db.query(models.Patient).filter(models.Patient.doctor_id == doctor_id).all()
