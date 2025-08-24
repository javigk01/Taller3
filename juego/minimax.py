from __future__ import annotations
from typing import Optional, Tuple
from .tablero import Tablero


class minimax:



    def elegir_mejor_jugada(self, tablero: Tablero, jugador_actual: str) -> Optional[Tuple[int, int]]:

        # implementamos aca el minimax con alfabeta.
        
        vacias = tablero.casillas_vacias()
        return vacias[0] if vacias else None
