from pydantic import BaseModel
import random

class Jogador(BaseModel):
    id: int
    nome: str
    dados: list[int] = []
    num_dados: int = 5

class Sala(BaseModel):
    sala_id: str
    host_id: int
    estado: str = "lobby"
    jogadores: list[Jogador] = []
    aposta_atual: dict | None = None
    turno_idx: int = 0

    def adicionar_jogador(self, jogador_id, nome):
        if self.estado != "lobby":
            raise ValueError("Jogo já começou.")
        if any(j.id == jogador_id for j in self.jogadores):
            return "Já está na sala."
        self.jogadores.append(Jogador(id=jogador_id, nome=nome))
        return self

    def iniciar_jogo(self, host_id):
        if host_id != self.host_id:
            raise ValueError("Somente o host pode iniciar o jogo.")
        self.estado = "jogando"
        random.shuffle(self.jogadores)
        self.rolar_dados()
        return self

    def rolar_dados(self):
        for j in self.jogadores:
            j.dados = [random.randint(1, 6) for _ in range(j.num_dados)]

    def fazer_aposta(self, acao):
        self.aposta_atual = {
            "jogador_id": acao.jogador_id,
            "quantidade": acao.quantidade,
            "valor": acao.valor
        }
        self.turno_idx = (self.turno_idx + 1) % len(self.jogadores)
        return self

    def duvidar(self, jogador_id):
        # apenas estrutura — coloque a lógica completa depois
        return {"resultado": "implementar lógica de duvida"}
