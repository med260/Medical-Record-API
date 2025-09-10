# main.py

import asyncio
from fastapi import FastAPI
from routes import auth, patients, doctors
from DB.database import engine
from models import Base

# --------------------- Create FastAPI app ---------------------
app = FastAPI(title="Medical Record API", version="1.0")

# --------------------- Include routers ---------------------
app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(doctors.router)

# --------------------- Root ---------------------
@app.get("/")
async def root():
    return {"message": "Welcome to the Medical Record API!"}

# --------------------- Create tables ---------------------
async def create_tables():
    async with engine.begin() as conn:
        # Use run_sync to execute the synchronous metadata creation
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully!")

# --------------------- Run create_tables if executed directly ---------------------
if __name__ == "__main__":
    asyncio.run(create_tables())
