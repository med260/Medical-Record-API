from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from DB.database import get_db

router = APIRouter(prefix="/patients", tags=["Patients"])


# @router.post("/", response_model=schemas.PatientResponse)
# async def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
#     return await crud.create_patient(db, patient)


@router.get("/{patient_id}", response_model=schemas.PatientResponse)
async def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = await crud.get_patient(db, patient_id)
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient


@router.get("/", response_model=list[schemas.PatientResponse])
async def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await crud.get_patients(db, skip=skip, limit=limit)


@router.delete("/{patient_id}", response_model=schemas.PatientResponse)
async def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = await crud.delete_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.post("/{patient_id}/assign_doctor/{doctor_id}", response_model=schemas.PatientResponse)
async def assign_doctor(patient_id: int, doctor_id: int, db: Session = Depends(get_db)):
    patient = await crud.assign_doctor_to_patient(db, doctor_id, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
