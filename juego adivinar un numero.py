import random
    

def main():
    m = 1
    t = 15
    numero_pc = random.randint(m,t)
    numero_elegido = int(input("adivina buen adivinador; "))
    while numero_elegido != numero_pc:
        if numero_elegido > t:
            print("fuaaaaa mucho numero, inenta con menos: ")
            numero_elegido = int(input("otra vez: "))
        if numero_elegido < numero_pc:
            print("un poco mas")
        else:
            print("menos menos")
        numero_elegido = int(input("intenta de nuevo: "))
    print("le atinaaaaaste")
        

if __name__ == "__main__":
    main()