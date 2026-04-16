import palavras
import palavras
import utils

def regras():
    print("O jogo e simples, o sistema ira gerar uma palavra aleatoria e cabe a voce tentar acerta-la. Voce tem 5 tentativas (ao errar a quinta o jogo sera finalizado). A palavra tem 4 letras. CASO VOCE CHUTE UMA PALAVRA E ERRE, O JOGO ACABARA IMEDIATAMENTE. CASO VOCE CHUTE UMA LETRA E ERRE, VOCE PERDERA UMA TENTATIVA. BOA SORTE!")
    print(f'aqui vai um exemplo de segredo: {palavras.gerar_segredo()}')


def ganhou_perdeu_aindaNenhum(resultado, segredo,escolha_usuario):
    global rodadas
    if escolha_usuario == 1:
        if resultado == segredo and rodadas <= 10:
            print(f"Parabens, voce acertou a palavra em {rodadas} tentativas")
            rodadas += 0
            return True
        elif resultado != segredo and rodadas <= 10:
            print(f"Voce ainda nao acertou a palavra, tente novamente")
            rodadas += 1
            return False
        else:
            print(f"Infelizmente voce nao acertou a palavra. A palavra era {segredo}")
            rodadas += 0
            return False
    else:
        if resultado == segredo:
            return True
        else:
            return False
    



def atualizadorLetras(resultado, segredo, funcao):
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
    
def verificaPalavra(resultado, segredo):
    if resultado == segredo:
        print("Parabens, voce acertou a palavra! Fim do jogo")
        return True
    else:
        print("Infelizmente voce nao acertou a palavra ao chutar. Fim do jogo")
        return False




def escolha():
    while True:
        escolha = input("desejar chuutar uma letra ou chutar uma palavra? (1/2):")
        try:
            escolha = int(escolha)
            if escolha in [1, 2]:
                return escolha   
            else:
                raise ValueError
        except ValueError:
            print("Escolha invalida, tente novamente")
        
        

rodadas = 0

def jogar():
    regras()
    segredo = palavras.gerar_segredo()
    while rodadas <= 11:
        print(f'voce esta na: {rodadas} rodada')
        escolha_usuario = escolha()
        if escolha_usuario == 1:
            chute = utils.pedir_chute(escolha_usuario)
            if rodadas == 0:
                resultado = utils.parcial(segredo, chute)
            resultado = atualizadorLetras(resultado, segredo, utils.parcial(segredo, chute))
            print(resultado)
            x = ganhou_perdeu_aindaNenhum(resultado, segredo, escolha_usuario)
            if x:
                break
            else:
                if rodadas <= 11 and x == False:
                    continue
                else:
                    break
        else:
            chute = utils.pedir_chute(escolha_usuario)
            if rodadas == 0:
                resultado = utils.parcial(segredo, chute)
            resultado = verificaPalavra(resultado, segredo)
            print(resultado)
            x = ganhou_perdeu_aindaNenhum(resultado, segredo)
            if x:
                break
            else:
                break
                

        
        
        
    





    

