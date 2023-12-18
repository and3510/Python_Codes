a=int(input())
b=int(input())
c=int(input())

mab=(a+b+abs(a-b))/2
mabc=(mab+c+abs(mab-c))/2
mabc=int(mabc)
d=(a+b+c)-mabc

if d==a+b:
   if a>b:
      print(b,a,mabc) 
   elif b>a:
      print(a,b,mabc)  
elif d==b+c:
    if b>c:
       print(c,b,mabc) 
    elif c>b:
       print(b,c,mabc) 
elif d==a+c:
    if a>c:
       print(c,a,mabc) 
    elif c>a:
       print(a,c,mabc)          

