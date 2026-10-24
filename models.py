from sqlalchemy import Column, String, DateTime
from datetime import datetime
from database import Base

class Participant(Base):
    __tablename__ = "participants"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=True)
    registration_time = Column(DateTime, default=datetime.utcnow)