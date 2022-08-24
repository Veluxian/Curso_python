def Conversor(moneda, dolares):
    moneda = float(input("ingresa cuanto dinero tienes : "))
                
    dolares = float(input("cuanto cuesta el dolar hoy : "))
  
    transformacion = moneda / dolares
    transformacion = str(round(transformacion, 2))

    print("tienes " + transformacion + " dolares")

def Again(again):
    again = str(input("para reiniciar ingresa R y para salir E "))

    if again.capitalize() == "R":
        Conversor(0,0)
        Again(0)
    elif again.capitalize() == "E":
        print("gracias por usar el conversor" )
    else:
        print("por no hacer caso me cierro")



start = input("para iniciar inrtesa S ")

if start.capitalize() == "S":
    Conversor(0,0)
    Again(0)
else: print("por no hacer caso me cierro ")
