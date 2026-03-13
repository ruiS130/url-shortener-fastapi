from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.db import Base


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String(length=2048), nullable=False)
    short_code = Column(String(length=64), unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    click_count = Column(Integer, nullable=False, default=0)

