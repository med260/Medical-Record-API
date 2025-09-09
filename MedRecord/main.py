from fastapi import FastAPI
from routes import auth
from routes import users, patients, doctors, ailments, prescriptions

# Create the app
app = FastAPI(title="Medical Record API", version="1.0")

app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(ailments.router)
app.include_router(prescriptions.router)
app.include_router(users.router)



@app.get("/")
def root():
    return {"message": "Welcome to the Medical Record API!"}



# create_tables.py
import asyncio
from DB.database import engine
from models import Base

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully!")

if __name__ == "__main__":
    asyncio.run(create_tables())
