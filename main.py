from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
import uuid

import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Celestius Backend Task", version="1.0")

MAX_CAPACITY = 50

class ParticipantCreate(BaseModel):
    name: str
    email: EmailStr
    department: str | None = None

@app.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: ParticipantCreate, db: Session = Depends(get_db)):
    current_count = db.query(models.Participant).count()
    if current_count >= MAX_CAPACITY:
        raise HTTPException(status_code=400, detail="Event is full")
    
    existing_participant = db.query(models.Participant).filter(models.Participant.email == data.email).first()
    if existing_participant:
        raise HTTPException(status_code=400, detail="Duplicate registration: Email already registered")
    
    new_participant = models.Participant(
        id=str(uuid.uuid4()),
        name=data.name,
        email=data.email,
        department=data.department
    )
    
    db.add(new_participant)
    db.commit()
    db.refresh(new_participant)
    
    return {
        "message": "Successfully registered!",
        "data": {
            "id": new_participant.id,
            "name": new_participant.name,
            "email": new_participant.email,
            "department": new_participant.department,
            "registration_time": new_participant.registration_time.isoformat()
        }
    }

@app.get("/registrations")
def get_registrations(db: Session = Depends(get_db)):
    participants = db.query(models.Participant).all()
    return {
        "total": len(participants),
        "registrations": [
            {
                "id": p.id,
                "name": p.name,
                "email": p.email,
                "department": p.department,
                "registration_time": p.registration_time.isoformat()
            } for p in participants
        ]
    }

@app.get("/registrations/{participant_id}")
def get_registration(participant_id: str, db: Session = Depends(get_db)):
    participant = db.query(models.Participant).filter(models.Participant.id == participant_id).first()
    if not participant:
        raise HTTPException(status_code=404, detail="Registration not found")
        
    return {
        "id": participant.id,
        "name": participant.name,
        "email": participant.email,
        "department": participant.department,
        "registration_time": participant.registration_time.isoformat()
    }