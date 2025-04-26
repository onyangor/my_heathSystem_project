from app import models, schemas
from sqlalchemy.orm import Session

def create_program(db: Session, program: schemas.ProgramCreate):
    db_program = models.Program(**program.dict())
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def enroll_client_in_program(db: Session, client_id: int, program_id: int):
    client = db.query(models.Client).get(client_id)
    program = db.query(models.Program).get(program_id)
    if not client or not program:
        raise ValueError("Client or Program not found")
    client.programs.append(program)
    db.commit()
    return {"message": "Client enrolled"}

def search_client_by_name(db: Session, name: str):
    return db.query(models.Client).filter(models.Client.name.ilike(f"%{name}%")).all()

def get_client_profile(db: Session, client_id: int):
    return db.query(models.Client).get(client_id)

def get_all_programs(db: Session):
    return db.query(models.Program).all()
