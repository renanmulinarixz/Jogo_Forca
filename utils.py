

class letra_invalida(Exception):
    pass

verificador = False
def pedir_chute(escolha_usuario):
    while verificador != True:
        chute = input("Digite um chute: ")
        if escolha_usuario == 1:
            if verificar_chute_letra(chute):
                return chute
            else:
                print("chute invalido, tente novamente")
        else:
            if verificar_chute_palavra(chute):
                return chute
            else:
                print("chute invalido, tente novamente")
        

def verificar_chute_letra(x):
    try:
        list(x)
        if isinstance(x, str) and len(x) == 1 and x.isalpha():
           return True
        else:
            raise letra_invalida
    except letra_invalida:
        return False
    
def verificar_chute_palavra(x):
    try:
        list(x)
        if isinstance(x, str) and len(x) == 4 and x.isalpha():
           return True
        else:
            raise letra_invalida
    except letra_invalida:
        return False
    



def parcial(segredo, chute, escolha_usuario):
    if escolha_usuario == 1:
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
    else:
        if chute == segredo:
            return True
        else:
            return False
    
       



