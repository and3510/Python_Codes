import random
a=random.randint(1,3)
b=int(input('Escolha uma arma:\n[1]tesoura\n[2]pedra\n[3]papel\n>>:'))
if 1<=b<=3:
    if a==b:
        print(b,a,'empate')
    elif a==1 and b==3 or a==2 and b==1 or a==3 and b==2:
        print(b,a,'perdeu')
    elif a==3 and b==1 or a==1 and b==2 or a==2 and a==3:
        print(b,a,'ganhou')  
else:
     print('numero invalido')              