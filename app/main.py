from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncpg
import asyncio
from typing import Optional

app = FastAPI()

# Modelo de dados para representar um aluno
class Aluno(BaseModel):
    turma: str
    matricula: str
    nome_completo: str
    nome_usuario: str
    senha: str

# Configurações do banco de dados
DATABASE_URL = "postgresql://postgres:Subwoofer1!@estoque-raiz.cl8g6mie0ys4.us-east-1.rds.amazonaws.com:5432/alunos"

# Função para conectar ao banco de dados
async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

# Endpoint GET para obter nome de usuário e senha do aluno por matrícula ou nome
@app.get("/alunos/")
async def get_aluno(matricula: Optional[str] = None, nome: Optional[str] = None):
    if not matricula and not nome:
        raise HTTPException(status_code=400, detail="É necessário fornecer a matrícula ou o nome do aluno")

    async with connect_to_db() as connection:
        if matricula:
            query = "SELECT nome_usuario, senha FROM alunos WHERE matricula = $1"
            aluno = await connection.fetchrow(query, matricula)
            if aluno:
                return {"nome_usuario": aluno['nome_usuario'], "senha": aluno['senha']}
            else:
                raise HTTPException(status_code=404, detail="Aluno não encontrado com esta matrícula")
        elif nome:
            query = "SELECT nome_usuario, senha FROM alunos WHERE LOWER(nome_completo) = $1"
            aluno = await connection.fetchrow(query, nome.lower())
            if aluno:
                return {"nome_usuario": aluno['nome_usuario'], "senha": aluno['senha']}
            else:
                raise HTTPException(status_code=404, detail="Aluno não encontrado com este nome")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)