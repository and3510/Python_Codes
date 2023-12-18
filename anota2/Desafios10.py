a=float(input())
b=float(input())
c=float(input())

if a<b+c and b<c+a and c<a+b and a!=0 and b!=0 and c!=0:
    print('forma um triangulo')
    if a==b==c:
         print('triangulo equilatero')
    elif a==b or b==c or a==c:
         print('triangulo isoceles')
    elif a!=b!=c:
         print('triangulo escaleno')  
else:
    print('nao forma um triangulo')               