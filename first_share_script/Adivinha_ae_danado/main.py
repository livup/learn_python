import random
print('*************')
print('* Jogo da adivinhação *')
print('*************')
numero_secreto = random.randint(1,20)
total_de_tentativas = 0
print('Você gosta de chocolates?' '\033[1m'+'\033[44m' +'\033[30m' + 'Quer ganhar um chocolate do Kadu?'+'\033[0;0m' 'Se sim, basta acertar o número no jogo da adivinhação :)')
print('Dica da sorte:')
print('\033[31m'+'o número escolhido está entre 1 e 20'+'\033[0;0m')
print('Você quer tentar em qual nível de dificuldade?')
print('\033[32m'+'\033[1m' + '(1) Fácil'+'\033[0;0m' '\033[34m'+'\033[1m' + '  (2) Médio''\033[31m' + '  (3) Difícil''\033[0;0m')
nivel = int(input('defina seu nível: '))
if(nivel == 1):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 5
else:
    total_de_tentativas = 3
for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite o seu número: '))
    print('você digitou: ', chute)
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if(acertou):
        print('você acertou :)')
        break
    elif(maior):
        print('eita! você errou! O seu chute foi maior que o número secreto')
    elif(menor):
        print('eita! você errou! O seu chute foi menor que o número secreto')
print('Fim de jogo!')