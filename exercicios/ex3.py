x = input("Qual o valor de x?")
y = input("Qual o valor de y?")


def comparar(x, y):
    if x < y:
        print(x, "e menor que", y)
    elif x > y:
        print(x, "e maior que", y)
    else:
        print(x, "e", y, "sao iguais!")


comparar(x, y)