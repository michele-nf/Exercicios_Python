x = int(input("Qual o valor de x?"))
y = int(input("Qual o valor de y?"))
z = int(input("Qual o valor de z?"))


def estaEntre(x, y, z):
    if y < x < z:
        return True
    else:
        return False


print(estaEntre(x, y, z))