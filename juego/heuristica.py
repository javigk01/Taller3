from __future__ import annotations
from .tablero import Tablero


def evaluar(tablero: Tablero, jugador_ia: str, jugador_humano: str) -> int:
    ganador = tablero.ganador()
    if ganador == jugador_ia:
        return 1
    elif ganador == jugador_humano:
        return -1
    elif tablero.esta_lleno():
        return 0
    return None # Para que el minimax sepa que el juego sigue

