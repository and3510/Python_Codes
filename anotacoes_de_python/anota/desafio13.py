a, b=input().split()
b=float(b)

if a=='A' and b<=20:
    c=b*(1.9*0.97)
    print('valor é',c)
elif a=='A' and b>20:
    c=b*(1.9*0.95)
    print('valor é',c)
elif   a=='G' and b<=20:
       c=b*(2.5*0.96) 
       print('o valor é',c) 
elif  a=='G' and b>20:  
       c=b*(2.5*0.94)
       print('o valor é',c)  


