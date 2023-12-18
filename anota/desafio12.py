a=int(input('digite um numero de 1 a 999:'))

if 1<=a<=999:
    c=a//100
    c1=a%100
    d=c1//10
    u=c1%10
    print('numero',a,'=',c,'centenas',d,'dezenas',u,'unidades') 
else:
 print('numero invalido') 



