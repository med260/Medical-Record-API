
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base
from config import settings
import logging
DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Set up detailed logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def get_db():
    async with AsyncSessionLocal() as db:  # ← Use async context manager
        try:
            yield db
        finally:
            await db.close()
# SQLAlchemy connection logging
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

