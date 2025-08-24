from __future__ import annotations
from typing import Optional
from .tablero import Tablero
from .minimax import minimax

#aqui esta el juego como tal resumido

class Juego:

    def __init__(self) -> None:
        self.tablero = Tablero()
        self.ia = minimax(jugador_max="X", jugador_min="O")
        self.jugador_humano = "O"
        self.jugador_ia = "X"

    def mostrar_tablero(self) -> None:
        print(self.tablero)
