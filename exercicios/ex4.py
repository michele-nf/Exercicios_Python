escolha = input("escolha a opcao A, B ou C: ")


def funcaoA():
    print("Voce escolheu a opcao A!")


def funcaoB():
    print("Voce escolheu a opcao B!")


def funcaoC():
    print("Voce escolheu a opcao C!")


def executar(escolha):
    if escolha == 'A':
        funcaoA()
    elif escolha == 'B':
        funcaoB()
    elif escolha == 'C':
        funcaoC()
    else:
        print("Escolha invalida!")


executar(escolha)
