print('\033[1:30:43m ..=>> Bem vindo ao JOKENPÔ!!! <<=.. \33[m\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))

print('Jo..')
sleep(1)
print('Ken...')
sleep(1)
print('Pô!!!!')

print('\033[1:30m-=\033[m' * 16)
print(f' O Computador escolheu >>{itens[computador]}') #faz escolher um ITEN na posição COMPUTADOR
print(f' O Jogador escolheu >>{itens[jogador]}')
print('\033[1:30m-=\033[m' * 16)

if computador == 0:
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCEU')

    elif jogador == 2:
        print('COMPUTADOR VENCEU')

    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCEU')

    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')

    elif jogador == 1:
        print('COMPUTADOR VENCEU')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVÁLIDA!')

else:
    print('JOGADA INVÁLIDA, REPITA!')
