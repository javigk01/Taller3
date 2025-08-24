from juego.juego import Juego


#la funcion del juego principal esta en la clase de juego porsia

def main():
    juego = Juego()
    print("Bienvenido a Triqui (3 en línea)")
    print("Tablero inicial:\n")
    print(juego.tablero)  # el tablerito


if __name__ == "__main__":
    main()
