a=float(input())
b=int(input())

br=a*b
print('o valor bruto é',br)
i=br*0.11
s=br*0.05
inss=br*0.08
sl=br-(i+s+inss)
print('o valor liquido é',sl)
