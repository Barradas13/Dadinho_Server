from fastapi import FastAPI, HTTPException
from rooms_manager import rooms_manager
from schemas import SalaCreate, EntrarSala, AcaoAposta

app = FastAPI(title="Dadinho API")

# Criar sala (gera ID aleatório e define host)
@app.post("/sala/criar")
def criar_sala(data: SalaCreate):
    sala = rooms_manager.criar_sala(data.host_id, data.host_nome)
    return sala

# Jogador entrando numa sala existente
@app.post("/sala/entrar")
def entrar_sala(data: EntrarSala):
    sala = rooms_manager.entrar_sala(data.sala_id, data.jogador_id, data.jogador_nome)
    return sala

# Host inicia jogo
@app.post("/sala/{sala_id}/iniciar")
def iniciar_jogo(sala_id: str, host_id: int):
    return rooms_manager.iniciar_jogo(sala_id, host_id)

# Jogador faz aposta
@app.post("/sala/{sala_id}/apostar")
def apostar(sala_id: str, acao: AcaoAposta):
    return rooms_manager.fazer_aposta(sala_id, acao)

# Jogador duvida
@app.post("/sala/{sala_id}/duvidar")
def duvidar(sala_id: str, jogador_id: int):
    return rooms_manager.duvidar(sala_id, jogador_id)

# Obter estado da sala
@app.get("/sala/{sala_id}")
def estado_sala(sala_id: str):
    return rooms_manager.estado_sala(sala_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)