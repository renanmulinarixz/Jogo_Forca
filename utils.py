

class letra_invalida(Exception):
    pass

verificador = False
def pedir_chute():
    while verificador != True:
        chute = input("Digite um chute: ")
        if verificar_chute(chute):
            return chute
        else:
            print("letra invalida, digite novamente")

def verificar_chute(x):
    try:
        list(x)
        if isinstance(x, str) and len(x) == 1 and x.isalpha():
           return True
        else:
            raise letra_invalida
    except letra_invalida:
        return False


def parcial(segredo, chute):
    segredo = list(segredo)
    parcial = []
    contador = 0
    for i in range(len(segredo)):
        if segredo[i] == chute:
            parcial.append(chute)
            contador += 1
        else:
            parcial.append("_")
    print(f"voce acerrtou {contador} letras")
    return "".join(parcial)
       

