import random


def generate_password():
    uppers = ["A", "B", "C", "D", "E", "F", "G"]
    lowers = ["a", "b", "c", "d", "e", "f", "g"]
    signs =  ["!", "#", "$", "%", "&", "/" , "("]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]

    caracteres = uppers + lowers + signs + numbers 

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password)
    return password

def main():
    password = generate_password()
    print("tu nueva contraseña es: " + password )

if __name__ == "__main__":
    main()