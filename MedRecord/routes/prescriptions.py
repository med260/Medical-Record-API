from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from DB.database import get_db

router = APIRouter(prefix="/prescriptions", tags=["Prescriptions"])


@router.post("/patient/{patient_id}", response_model=schemas.PrescriptionResponse)
def create_prescription(patient_id: int, prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db)):
    return crud.create_prescription(db, prescription, patient_id)


@router.get("/", response_model=list[schemas.PrescriptionResponse])
def read_prescriptions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_prescriptions(db, skip=skip, limit=limit)


@router.delete("/{prescription_id}", response_model=schemas.PrescriptionResponse)
def delete_prescription(prescription_id: int, db: Session = Depends(get_db)):
    prescription = crud.delete_prescription(db, prescription_id)
    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return prescription
