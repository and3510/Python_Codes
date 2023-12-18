a=float(input())
b=float(input())
c=float(input())

if a>b+c or b>c+a or c>a+b or a==0 or b==0 or c==0:
   print('Nao forma um triangulo')
else:
   if a==b==c:
    print('Equilatero')
   else:
     if a==b or c==a or b==c:
       print('isoceles')
     else:
       print('escaleno')       
