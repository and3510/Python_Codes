a=str(input('nome da conta:'))
b=float(input('digite seu saldo:'))
c=float(input('digite seu debito:'))
d=float(input('digite seu credito:'))

sa=b-(c+d)
if sa>=0:
    print('Saldo positivo')
else:
     print('Saldo Negativo')    