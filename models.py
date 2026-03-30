from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from datetime import datetime
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True)
    name = Column(String)
    email = Column(String)
    embedding = Column(LargeBinary)


class VerificationLog(Base):
    __tablename__ = "verification_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    similarity = Column(String)
    result = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)