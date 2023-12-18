a=str(input('nome do individuo:'))
b=int(input('ano do nascimento:'))
c=int(input('ano de ingresso no trabalho:'))

if 2023-b>=65 and 2023-c>=30:
    print('Requerer aposentadoria')
else:
   if 2023-b>=60 and 2023-c>=25:
    print('Requerer aposentadoria')
   else:
      print('Nao requerer')     