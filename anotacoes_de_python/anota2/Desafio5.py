import random
a=int(input())
b=random.randint(1,10)

while a!=b:
    print('Errou! tente de novo')
    a=int(input())   
    if 1<=a<=10:
       if a==b:
          print('Parabéns voce acertou')
    else:
        print('numero invalido')             