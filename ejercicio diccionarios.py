# esto es una lista
# numeros = [1, 2, 3, 4]


# agregar elemento metodo append
# ejemplo numeros.append(False)
# borrar elemento metodo pop
# numeros.pop(2) (se leimina el 3)


# Tuplas ahorra datos, mejor que la lista en este caso

# mi_tupla = (1, 2, 3, 4, 5)

# no se pueden agregar ni quitar cosas
# al momento de meter la tupla al ciclo "for" es mas rapida y usa menos datos


# diccionarios

def main():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    print(mi_diccionario["llave1"])


    poblacion_pais = {
        "chile": 7523000,
        "brazil": 95246300,
        "canada": 74411202,
    }
    print(poblacion_pais["chile"])

    # metodo .keys entrega las llaves
    # metodo .values entrega los valores de las llaves
    # metodo .items entrega ambos casos 
    for pais, poblacion in poblacion_pais.items():
        print("el pais " + pais + " tiene " + str(poblacion) + " habitantes.")


if __name__ == "__main__":
    main()