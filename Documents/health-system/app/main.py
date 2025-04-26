from fastapi import FastAPI, HTTPException
from app import models, schemas, crud, database
from sqlalchemy.orm import Session
from typing import List

from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
database.Base.metadata.create_all(bind=database.engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/programs", response_model=schemas.Program)
def create_program(program: schemas.ProgramCreate, db: Session = Depends(database.get_db)):
    return crud.create_program(db, program)

@app.post("/clients", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(database.get_db)):
    return crud.create_client(db, client)

@app.post("/enroll")
def enroll_client(client_id: int, program_id: int, db: Session = Depends(database.get_db)):
    return crud.enroll_client_in_program(db, client_id, program_id)

@app.get("/clients/search")
def search_client(name: str, db: Session = Depends(database.get_db)):
    return crud.search_client_by_name(db, name)

@app.get("/clients/{client_id}", response_model=schemas.ClientProfile)
def get_client_profile(client_id: int, db: Session = Depends(database.get_db)):
    return crud.get_client_profile(db, client_id)

@app.get("/programs", response_model=List[schemas.Program])
def get_all_programs(db: Session = Depends(database.get_db)):
    programs = crud.get_all_programs(db)
    return programs
