altura = int(input("A multiplicacao vai ate que numero? Numero: "))
n = int(input("A tabuada vai ate que numero? Numero: "))


def imprimeMultiplos(n, altura):
    i = 1
    while i <= altura:
        print(n * i, '\t'),
        i = i + 1
        print()


def imprimeTabMult(altura):
    i = 1
    while i <= altura:
        imprimeMultiplos(i, altura)
        i = i + 1


print(imprimeTabMult(altura))