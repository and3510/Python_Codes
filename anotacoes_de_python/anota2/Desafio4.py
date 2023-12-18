a=float(input('Seu salario anual:'))
b=int(input('total de dependentes:'))
c=(a/12)/(b+1)

if c<=1903.98:
     print('isento de imposto')
elif 1903.99<=c<=2826.65:
     vf=c*0.075+142.80
     print('%.2f'%vf)
elif 2826.66<=c<=3751.05:
     vf=c*0.15+354.80
     print('%.2f'%vf)
elif 3751.06<=c<=4664.68:
     vf=c*0.225+636.13
     print('%.2f'%vf)
elif c>4664.68:
     vf=c*0.275+869.36
     print('%.2f'%vf)
   




        

  