from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from DB.database import get_db
import schemas, models

router = APIRouter(prefix="/records", tags=["medical_records"])

# Create a record
@router.post("/", response_model=schemas.MedicalRecordResponse)
async def create_record(record: schemas.MedicalRecordCreate, db: AsyncSession = Depends(get_db)):
    db_record = models.MedicalRecord(**record.model_dump())
    db.add(db_record)
    await db.commit()
    await db.refresh(db_record)
    return db_record

# Get a single record
@router.get("/{record_id}", response_model=schemas.MedicalRecordResponse)
async def get_record(record_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.MedicalRecord).where(models.MedicalRecord.id == record_id))
    record = result.scalar()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record

# Get all records
@router.get("/", response_model=list[schemas.MedicalRecordResponse])
async def get_records(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.MedicalRecord).offset(skip).limit(limit))
    records = result.scalars().all()
    return records

# Update a record
@router.put("/{record_id}", response_model=schemas.MedicalRecordResponse)
async def update_record(record_id: int, updated_data: schemas.MedicalRecordCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.MedicalRecord).where(models.MedicalRecord.id == record_id))
    record = result.scalar()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    for key, value in updated_data.model_dump().items():
        setattr(record, key, value)
    await db.commit()
    await db.refresh(record)
    return record

# Delete a record
@router.delete("/{record_id}")
async def delete_record(record_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.MedicalRecord).where(models.MedicalRecord.id == record_id))
    record = result.scalar()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    await db.delete(record)
    await db.commit()
    return {"detail": "Record deleted"}
