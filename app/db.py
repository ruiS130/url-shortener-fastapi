import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    # Example: postgresql://postgres:password@localhost:5432/url_shortener
    "postgresql://postgres:postgres@localhost:5432/url_shortener",
)

engine = create_engine(DATABASE_URL, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

