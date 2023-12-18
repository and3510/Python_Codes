#desafio 1
import random
a=random.randint(1,10)
b=int(input('escreva o numero de 1 a 10:'))

if 1<=b<=10:
   if b==a:
      print('Parabens voce acertou')
   else: print('Voce errou o valor era',a)
else: print('numero invalido')     

