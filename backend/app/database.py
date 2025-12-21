from sqlmodel import create_engine, SQLModel, Session
from app.config import settings

# Create database engine
engine = create_engine(
    settings.database_url,
    echo=True,  # Log SQL queries (set to False in production)
    pool_pre_ping=True,  # Verify connections before using them
    pool_size=5,
    max_overflow=10
)


def create_db_and_tables():
    """Create all database tables"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency for getting database session"""
    with Session(engine) as session:
        yield session
