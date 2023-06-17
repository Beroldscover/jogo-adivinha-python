from random import randint
from time import sleep
maquina = randint (0, 5) # o pc vai pensar nessa probabilidade

print ('~' * 50)
print ('Olá, Sou a maquina que encontra magos dos PC!!')
print ('~' * 50)
jogador = int (input('Escolha um numero de 0 á 5 se for capaz: '))
print ('~' * 50)
print ('HMMM...')
print ('~' * 12)
sleep (1.5)
print ('Você é..')
print ('~' * 12)
sleep (2)
if jogador == maquina:
    print ('Um mago implacavel, você pensou no numero: {} e eu tambem pensei no numero: {}'.format(jogador, maquina))
else:
    print ('Uma farsa pensei {} e você falou {} saia daqui..'.format(maquina, jogador))

