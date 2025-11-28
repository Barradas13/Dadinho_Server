from pydantic import BaseModel

class SalaCreate(BaseModel):
    host_id: int
    host_nome: str

class EntrarSala(BaseModel):
    sala_id: str
    jogador_id: int
    jogador_nome: str

class AcaoAposta(BaseModel):
    jogador_id: int
    quantidade: int
    valor: int
