# import asyncio
# from DB.database import AsyncSessionLocal
# from models import User, Patient, Doctor
# from routes.auth import get_password_hash

# async def create_fake_data():
#     async with AsyncSessionLocal() as db:
#         # Create test users
#         users = [
#             User(
#                 username="john_patient",
#                 email="john@example.com",
#                 hashed_password=get_password_hash("patient123"),
#                 is_active=True
#             ),
#             User(
#                 username="dr_smith", 
#                 email="smith@hospital.com",
#                 hashed_password=get_password_hash("doctor123"),
                
#                 is_active=True
#             )
#         ]
        
#         # Create test patients
#         patients = [
#             Patient(
#                 name="John Doe",
#                 age=35,
#                 gender="Male"
#             )
#         ]
        
#         # Create test doctors
#         doctors = [
#             Doctor(
#                 name="Dr. Smith",
#                 specialization="Cardiology"
#             )
#         ]

#         db.add_all(users + patients + doctors)
#         await db.commit()
#         print("✅ Fake data created successfully!")

# if __name__ == "__main__":
#     asyncio.run(create_fake_data())


# recreate_tables.py
import asyncio
from DB.database import engine
from models import Base

async def recreate_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)  # Drops all tables
        await conn.run_sync(Base.metadata.create_all)  # Creates new ones
    print("Tables recreated!")

asyncio.run(recreate_tables())