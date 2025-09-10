# routes/auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from DB.database import get_db
import models, schemas
from config import settings
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

router = APIRouter(prefix="/auth", tags=["auth"])

# ------------------- Security helpers -------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
blacklisted_tokens = set()

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)  # Remove async/await

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Remove async

def create_refresh_token(data: dict):
    expire = datetime.now() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Remove async
# ------------------- Routes -------------------
@router.post("/register", response_model=schemas.PatientResponse | schemas.DoctorResponse)
async def register(user: schemas.PatientCreate | schemas.DoctorCreate, db: AsyncSession = Depends(get_db)):
    Model = models.Patient if getattr(user, "role", "patient") == "patient" else models.Doctor

    # ✅ Check if email already exists
    existing_user = await db.execute(select(models.User).where(models.User.email == user.email))
    if existing_user.scalar():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = get_password_hash(user.password)

    if Model == models.Patient:
        new_user = models.Patient(
            username=user.username,   # ✅ important
            email=user.email,
            name=user.name,
            hashed_password=hashed_pw,
            age=user.age,
            gender=user.gender,
        )
    else:
        new_user = models.Doctor(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw,
        name=user.name,   # 👈 add this line
        specialization=user.specialization,
        years_of_experience=user.years_of_experience,
    )


    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.post("/login", response_model=schemas.Token)
async def login(credentials: schemas.UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(models.User).where(models.User.email == credentials.email)
    )
    user = result.scalar()
    
    if not user or not pwd_context.verify(credentials.password, user.hashed_password):  # FIXED
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    # Create tokens
    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    refresh_token = create_refresh_token(data={"sub": user.username})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "refresh_token": refresh_token
    }