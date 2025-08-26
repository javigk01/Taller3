from __future__ import annotations
from typing import Optional, Tuple
from .tablero import Tablero
from .heuristica import evaluar

class minimax:

    def elegir_mejor_jugada(self, tablero: Tablero, jugador_ia: str, jugador_humano: str) -> Optional[Tuple[int, int]]:
        _, mejor_mov = self._minimax(tablero, 0, float('-inf'), float('inf'), True, jugador_ia, jugador_humano)
        return mejor_mov
        # implementamos aca el minimax con alfabeta.


    def _minimax(self, tablero: Tablero, profundidad: int, alfa: float, beta: float, maximizando: bool,
                     jugador_ia: str, jugador_humano: str):
            valor = evaluar(tablero, jugador_ia, jugador_humano)
            if valor is not None:
                return valor, None

            if maximizando:
                max_eval = float('-inf')
                mejor_mov = None
                for (i, j) in tablero.casillas_vacias():
                    nuevo_tablero = Tablero()
                    nuevo_tablero.tablero = [fila[:] for fila in tablero.tablero]
                    nuevo_tablero.colocar(i, j, jugador_ia)
                    eval, _ = self._minimax(nuevo_tablero, profundidad + 1, alfa, beta, False, jugador_ia,
                                            jugador_humano)
                    if eval > max_eval:
                        max_eval = eval
                        mejor_mov = (i, j)
                    alfa = max(alfa, eval)
                    if beta <= alfa:
                        break
                return max_eval, mejor_mov
            else:
                min_eval = float('inf')
                mejor_mov = None
                for (i, j) in tablero.casillas_vacias():
                    nuevo_tablero = Tablero()
                    nuevo_tablero.tablero = [fila[:] for fila in tablero.tablero]
                    nuevo_tablero.colocar(i, j, jugador_humano)
                    eval, _ = self._minimax(nuevo_tablero, profundidad + 1, alfa, beta, True, jugador_ia,
                                            jugador_humano)
                    if eval < min_eval:
                        min_eval = eval
                        mejor_mov = (i, j)
                    beta = min(beta, eval)
                    if beta <= alfa:
                        break
                return min_eval, mejor_mov
