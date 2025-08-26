from juego.juego import Juego
from typing import Optional, Tuple
from juego.tablero import Tablero
from juego.heuristica import evaluar

#la funcion del juego principal esta en la clase de juego porsia

def main():
    juego = Juego()
    print("Bienvenido a Triqui (3 en línea)")
    print("Tablero inicial:\n")
    print(juego.tablero)  # el tablerito
    juego.jugar()


if __name__ == "__main__":
    main()
