def Main():
    palabra = input("escribe algo : ")
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[ : :-1]
    if palabra == palabra_invertida:
        print("Si es un palindromo")
    else:
        print("try again")


if __name__ == '__main__':
    Main()

