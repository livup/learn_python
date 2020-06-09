import random
def teste():
    print("""Bem vindo ao jogo da velha, o jogo funciona da seguinte maneira:
      Você deverá escolher um número entre 1 e 9, que não seja repetido, para apontar onde você quer jogar:
      Ao escolher seu número a máquina irá escolher o dela e assim irão jogando até o jogo terminar
      """)
    print("""Jogo começando, você começa! Escolha seu número
         0 | 1 | 2
         3 | 4 | 5
         6 | 7 | 8""")
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    numero_escolhido = input("Qual posição você quer escolher?")
    numero_escolhido = int(numero_escolhido)
    i = 1
    while i <= 5:
        if numero_escolhido in lista:
            lista[numero_escolhido] = 'x'
            numero_pc = random.randrange(0,8,1)
            while numero_pc not in lista:
                numero_pc = random.randrange(0, 8, 1)
            lista[numero_pc]='o'
            print(f"""
                {lista[0]} | {lista[1]} | {lista[2]}
                {lista[3]} | {lista[4]} | {lista[5]}
                {lista[6]} | {lista[7]} | {lista[8]}""")
            i += 1
            if lista[0]== 'x' and lista[1] == 'x' and lista[2] == 'x' or \
                lista[3]== 'x' and lista[4] == 'x' and lista[5] == 'x' or \
                lista[6] == 'x' and lista[7] == 'x' and lista[8] == 'x' or \
                lista[0] == 'x' and lista[3] == 'x' and lista[6] == 'x' or \
                lista[1] == 'x' and lista[4] == 'x' and lista[7] == 'x' or \
                lista[2] == 'x' and lista[5] == 'x' and lista[8] == 'x' or \
                lista[0] == 'x' and lista[4] == 'x' and lista[8] == 'x' or \
                lista[2] == 'x' and lista[4] == 'x' and lista[6] == 'x' :
                    print("Você ganhou.")
                    break
            else:
                if lista[0] == 'o' and lista[1] == 'o' and lista[2] == 'o' or \
                lista[3] == 'o' and lista[4] == 'o' and lista[5] == 'o' or \
                lista[6] == 'o' and lista[7] == 'o' and lista[8] == 'o' or \
                lista[0] == 'o' and lista[3] == 'o' and lista[6] == 'o' or \
                lista[1] == 'o' and lista[4] == 'o' and lista[7] == 'o' or \
                lista[2] == 'x' and lista[5] == 'x' and lista[8] == 'x' or \
                lista[0] == 'o' and lista[4] == 'o' and lista[8] == 'o' or \
                lista[2] == 'o' and lista[4] == 'o' and lista[6] == 'o':
                    print("Você perdeu.")
                    break
        else:
            print("Número escolhido fora do range")
            numero_escolhido = int(input("Qual posição você quer escolher?"))
teste()