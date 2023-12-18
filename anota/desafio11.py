a=int(input('Digite um ano:'))

if a%4==0 and a%100!=0:
    print('ano bissexto')
else:
    if a%4==0 and a%100==0 and a%400==0:
      print('ano bissexto')
    else:
        print('ano nao bissexto')        