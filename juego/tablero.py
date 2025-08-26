from __future__ import annotations
from typing import List, Optional, Tuple


class Tablero:

    #definicion del tablaero
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]


    def colocar(self, fila: int, col: int, ficha: str) -> bool:
        if self.tablero[fila][col] == ' ':
            self.tablero[fila][col] = ficha
            return True
        return False

    def casillas_vacias(self) -> List[Tuple[int, int]]:
        vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == ' ':
                    vacias.append((i, j))
        return vacias

    def ganador(self) -> Optional[str]:
        #filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != ' ':
                return fila[0]
        #columnas
        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] != ' ':
                return self.tablero[0][col]
        #diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            return self.tablero[0][2]
        return None

    def esta_lleno(self) -> bool:
        return all(self.tablero[i][j] != ' ' for i in range(3) for j in range(3))

    def __str__(self) -> str:
        filas = [' | '.join(self.tablero[i]) for i in range(3)]
        return '\n---------\n'.join(filas)