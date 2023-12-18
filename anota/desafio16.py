a=int(input('escreva o codigo:'))

if a==1234:
   b=int(input('escreva a senha:'))
   if b==9999:
      print('Acesso permitido')
   else:
       print('senha incorreta') 
else:
   print('Usuario invalido')