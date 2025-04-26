from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

client_program = Table(
    'client_program', Base.metadata,
    Column('client_id', Integer, ForeignKey('clients.id')),
    Column('program_id', Integer, ForeignKey('programs.id'))
)

class Program(Base):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    contact = Column(String)
    programs = relationship("Program", secondary=client_program, backref="clients")
