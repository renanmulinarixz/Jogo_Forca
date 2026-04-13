import palavras
import palavras
import utils
from colorama import Fore, Style

def regras():
    print("O jogo e simples, o sistema ira gerar uma palavra aleatoria e cabe a voce tentar acerta-la. Voce tem 5 tentativas (ao errar a quinta o jogo sera finalizado). A palavra tem 4 letras")
    print(f'aqui vai um exemplo de segredo: {palavras.gerar_segredo()}')


def ganhou_perdeu_aindaNenhum(resultado, segredo):
    global rodadas
    if resultado == segredo and rodadas <= 10:
        print(f"{Fore.GREEN}Parabens, voce acertou a palavra em {rodadas} tentativas{Style.RESET_ALL}")
        rodadas += 0
        return True
    elif resultado != segredo and rodadas <= 10:
        print(f"{Fore.YELLOW}Voce ainda nao acertou a palavra.{Style.RESET_ALL}")
        rodadas += 1
        return False
    else:
        print(f"{Fore.RED}Infelizmente voce nao acertou a palavra. A palavra era {segredo}{Style.RESET_ALL}")
        rodadas += 0
        return False



def atualiza(resultado, segredo, funcao):
    x = list(funcao)
    if resultado == segredo:
        return False
    else:
        resultado = list(resultado)
        for i in range(len(segredo)):
            if funcao[i] == resultado[i]:
                resultado[i] = resultado[i]
            else:
                if funcao[i] != "_":
                    resultado[i] = funcao[i]
        return "".join(resultado)


rodadas = 0

def jogar():
    regras()
    segredo = palavras.gerar_segredo()
    while rodadas <= 11:
        print(f'voce esta na: {rodadas} rodada')
        chute = utils.pedir_chute()
        if rodadas == 0:
            resultado = utils.parcial(segredo, chute)
        resultado = atualiza(resultado, segredo, utils.parcial(segredo, chute))
        print(resultado)
        x = ganhou_perdeu_aindaNenhum(resultado, segredo)
        if x:
            break
        else:
            if rodadas <= 11 and x == False:
                continue
            else:
                break
        
    





    

