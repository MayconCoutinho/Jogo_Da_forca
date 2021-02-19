# Resolver: [] Acerta apenas uma vez a letra chave ou as letras 
#


palavra_chave = str(input('Difite a palavra chave: '))
caracteres = list(palavra_chave)
chaves = len(caracteres) # Quantidades de chaves para libera (cada acerto é uma chave)
tentativas = 10
acertos = 0
erro = 0 
ganhou = 0


while tentativas != 0:
    chute = str(input('Chute uma letra: '))
    
    for contador in range(0,(chaves)):
        # variáveis 
        comparador = caracteres[(contador)]
        chute_certo = 0
        
        if chute == comparador:
            chute_certo = chute_certo +1 
            print('Você acerto a letra {0} falta {1}/{2}'.format(chute,acertos+1,chaves))


        elif chute != comparador:
            erro = erro + 1
        else:
            print('ERRO....ERRO....ERRO.....')

        if chute_certo == 1:
            print('você acertou a letra {}'.format(chute))
            acertos = acertos + 1
            chute_certo = chute_certo -1
            

        

        if acertos == chaves:
            tentativas = 0
            ganhou = 1
            break

        elif erro == chaves:
            tentativas = tentativas -1 
            print('você errou o chute você tem mais  {} tentativas'.format(tentativas))
            erro = 0

    
         
        
        
if  ganhou == 0:
    print('Você perdeu')
elif ganhou == 1:
    print("VOCÊ GANHOU!!!")
else:
    print('ERRO...ERRO...ERRO')
    

        
        
