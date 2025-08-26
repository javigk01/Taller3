from __future__ import annotations
from typing import Optional
from .tablero import Tablero
from .minimax import minimax

#aqui esta el juego como tal resumido

class Juego:

    def __init__(self) -> None:
        self.tablero = Tablero()
        self.minimax = minimax()
        self.jugador_humano = "O"
        self.jugador_ia = "X"

    def jugar(self):
        turno_ia = False  # El humano siempre inicia
        while True:
            print(self.tablero)
            if self.tablero.ganador() or self.tablero.esta_lleno():
                break
            if turno_ia:
                print("Turno de la IA...")
                mov = self.minimax.elegir_mejor_jugada(self.tablero, self.jugador_ia, self.jugador_humano)
                if mov:
                    self.tablero.colocar(mov[0], mov[1], self.jugador_ia)
            else:
                while True:
                    try:
                        fila = int(input("Fila (0-2): "))
                        col = int(input("Columna (0-2): "))
                        if 0 <= fila < 3 and 0 <= col < 3 and self.tablero.colocar(fila, col, self.jugador_humano):
                            break
                        else:
                            print("Casilla ocupada o fuera de rango, intenta de nuevo.")
                    except Exception:
                        print("Entrada inválida, intenta de nuevo.")
            turno_ia = not turno_ia
        print(self.tablero)
        ganador = self.tablero.ganador()
        if ganador == self.jugador_humano:
            print("¡Ganaste!")
        elif ganador == self.jugador_ia:
            print("¡La IA gana!")
        else:
            print("¡Empate!")
