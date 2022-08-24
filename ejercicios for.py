def main():

#    nombre = input("Cual es tu nombre : ")
#    for letra in nombre :
#        print(letra)


#    frase = input("escribe una frase: ")
#    for caracter in frase:
#     print(caracter.upper())

    # for contador in range(101):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    # for i in range(101):
    #     print(i)
    #     if i == 57:
    #         break
    
    texto = input("escribe algo : ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__ == "__main__" :
    main()