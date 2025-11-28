import uuid
from models import Sala

class RoomsManager:
    def __init__(self):
        self.salas = {}  # sala_id → Sala

    def criar_sala(self, host_id, host_nome):
        sala_id = uuid.uuid4().hex[:6].upper()
        sala = Sala(sala_id=sala_id, host_id=host_id)
        sala.adicionar_jogador(host_id, host_nome)
        self.salas[sala_id] = sala
        return sala

    def entrar_sala(self, sala_id, jogador_id, nome):
        if sala_id not in self.salas:
            raise ValueError("Sala inexistente.")
        return self.salas[sala_id].adicionar_jogador(jogador_id, nome)

    def iniciar_jogo(self, sala_id, host_id):
        sala = self.salas[sala_id]
        return sala.iniciar_jogo(host_id)

    def fazer_aposta(self, sala_id, acao):
        sala = self.salas[sala_id]
        return sala.fazer_aposta(acao)

    def duvidar(self, sala_id, jogador_id):
        sala = self.salas[sala_id]
        return sala.duvidar(jogador_id)

    def estado_sala(self, sala_id):
        return self.salas[sala_id]

rooms_manager = RoomsManager()
