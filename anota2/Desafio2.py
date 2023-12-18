b=float(input('escreva um valor:'))
a=int(input('Escolha uma forma de pagamento:\n[1]CREDITO\n[2]DEBITO\n[3]Pix\n[4]Especie\n>>:'))

if 1<=a<=4:
   if a==3:
       s=b*0.9
       print(s)
   elif a==2:
         s=b*0.95
         print(s)
   elif a==1:
        c=int(input('em quantas vezes:\n[1]ate duas vezes\n[2]ate mais que tres vezes\n>>:'))   
        if c==1:
           print(b)
        if c==2:
           s=b*1.2
           print(s)  
   elif a==4:
        print(b)       
else: print('numero invalido')                  