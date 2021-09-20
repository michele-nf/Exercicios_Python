x1 = int(input("Digite o valor de X1:"))
x2 = int(input("Digite o valor de X2:"))
y1 = int(input("Digite o valor de Y1:"))
y2 = int(input("Digite o valor de Y2:"))


def coeficienteAngular(x1, y1, x2, y2):
    coeficiente_angular = (y2 - y1) / (x2 - x1)
    print(coeficiente_angular)


coeficienteAngular(x1, y1, x2, y2)
