from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5000/hospital_db"

engine = create_engine(DATABASE_URL , echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")

if __name__ == "__main__":
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()