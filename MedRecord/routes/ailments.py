from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from DB.database import get_db

router = APIRouter(prefix="/ailments", tags=["Ailments"])


@router.post("/patient/{patient_id}", response_model=schemas.AilmentResponse)
async def create_ailment(patient_id: int, ailment: schemas.AilmentCreate, db: Session = Depends(get_db)):
    return await crud.create_ailment(db, ailment, patient_id)


@router.get("/", response_model=list[schemas.AilmentResponse])
async def read_ailments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await crud.get_ailments(db, skip=skip, limit=limit)


@router.get("/patient/{patient_id}", response_model=list[schemas.AilmentResponse])
async def get_patient_ailments(patient_id: int, db: Session = Depends(get_db)):
    return await crud.get_patient_ailments(db, patient_id)


@router.delete("/{ailment_id}", response_model=schemas.AilmentResponse)
async def delete_ailment(ailment_id: int, db: Session = Depends(get_db)):
    ailment = await crud.delete_ailment(db, ailment_id)
    if not ailment:
        raise HTTPException(status_code=404, detail="Ailment not found")
    return ailment
