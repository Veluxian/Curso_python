def main():
    TOPE = 1000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < TOPE:
        print(potencia_2)
        contador = contador + 1
        potencia_2 = 2**contador
        if potencia_2 == 8:
            break


if __name__ == "__main__":
    main()

    