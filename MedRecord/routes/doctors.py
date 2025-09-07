from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from DB.database import get_db

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.post("/", response_model=schemas.DoctorResponse)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db, doctor)


@router.get("/{doctor_id}", response_model=schemas.DoctorResponse)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor(db, doctor_id)
    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor


@router.get("/", response_model=list[schemas.DoctorResponse])
def read_doctors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_doctors(db, skip=skip, limit=limit)


@router.get("/{doctor_id}/patients", response_model=list[schemas.PatientResponse])
def get_doctor_patients(doctor_id: int, db: Session = Depends(get_db)):
    return crud.get_doctor_patients(db, doctor_id)
