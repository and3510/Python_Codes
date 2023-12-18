a=float(input('valor em real:'))
b=float(input('peso:'))
d=a/5
if d>100:
    print('será taxado')
    if 100<a<200:
     t=b*3
     s=a+t
     print(s)
    else:
     t=b*4.25
     s=a+t
     print(s)
else:     
    print('sem taxaçao',a)