from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "postgresql://postgres:Subwoofer1!@estoque-raiz.cl8g6mie0ys4.us-east-1.rds.amazonaws.com:5432/AlunosPlurall"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    turma = Column(String)
    matricula = Column(String, unique=True, index=True)
    nome_completo = Column(String)
    nome_usuario = Column(String)
    senha = Column(String)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

def get_aluno_details(matricula_nome: str):
    session = SessionLocal()
    aluno = session.query(Aluno).filter(Aluno.nome_completo == matricula_nome).first()
    session.close()
    return aluno

def get_aluno_byCod(matricula_cod: str):
    session = SessionLocal()
    aluno = session.query(Aluno).filter(Aluno.matricula == matricula_cod).first()
    session.close()
    return aluno

@app.get("/alunos/")
async def get_aluno(matricula_nome: str):
    aluno = get_aluno_details(matricula_nome)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return JSONResponse(content={"nome_usuario": aluno.nome_usuario, "senha": aluno.senha}, headers={"Access-Control-Allow-Origin": "*"})
    
@app.get("/alunosCod/")
async def get_aluno(matricula: str):
    aluno = get_aluno_byCod(matricula)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return JSONResponse(content={"nome_usuario": aluno.nome_usuario, "senha": aluno.senha}, headers={"Access-Control-Allow-Origin": "*"})