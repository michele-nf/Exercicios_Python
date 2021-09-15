x = int(input("Qual o valor de x?"))
y = int(input("Qual o valor de y?"))


def comparar(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


print(comparar(x, y))