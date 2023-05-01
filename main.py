from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada ? '))
print('\033[1;35mJO\033[m')
sleep(1)
print('\033[1;35mKEN\033[m')
sleep(1)
print('\033[1;35mPO!!!\033[m')
print('-=-' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=-' * 10)
if computador == 0:
    if jogador == 0:
        print('\033[1;33mEMPATE\033[m!')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCE\033[m!')
    elif jogador == 2:
        print('\033[1;36mCOMPUTADOR VENCE\033[m!')
    else:
        print('\033[1;31JOGADA INVÁLIDA!\033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[1;36mCOMPUTADOR VENCE\033[m!')
    elif jogador == 1:
        print('\033[1;33mEMPATE\033[m!')
    elif jogador == 2:
        print('\033[1;32mJOGADOR VENCE\033[m!')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[1;32mJOGADOR VENCE\033[m!')
    elif jogador == 1:
        print('\033[1;36mCOMPUTADOR VENCE\033[m!')
    elif jogador == 2:
        print('\033[1;33mEMPATE\033[m!')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')

