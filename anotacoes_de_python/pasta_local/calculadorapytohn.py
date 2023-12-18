

def calculadora(a,b,c): 
    if Calculo ==0:
        h=numero1+numero2
        print('resultado =',h)
        return h
    elif Calculo ==1:
        h=numero1-numero2
        print('resultado =',h)
        return h
    elif Calculo ==2:
        h=numero1*numero2
        print('resultado =',h)
        return h
    elif Calculo ==3:
        h=numero1//numero2
        print('resultado =',h)
        return h

    

    
while True:
    print('[0]-Soma\n'
    '[1]-Subtraçao\n'
    '[2]-Multiplicaçao\n'
    '[3]-Divisao\n'
    '[4]-Desligar')
    Calculo=int(input())
    if Calculo== 4:
        print('finalizado')
        break
    if Calculo>4:
        print('numero invalido! tente novamente')
        break
    numero1=int(input())
    numero2=int(input())
    m=calculadora(Calculo,numero1,numero2)
    print(m)
    
    while True:
        print('[0]-quer finalizar o calculo\n'
            '[9]-acrencentar um novo valor no calculo')
        ç=int(input())
        if ç==0:
            print(m)
            break
            
        elif ç==9:
            print('[0]-Soma\n'
            '[1]-Subtraçao\n'
            '[2]-Multiplicaçao\n'
            '[3]-Divisao')
            j=int(input('digite a forma de calculo:'))
            n=int(input('digite um novo valor:'))
            if j==0:
                m=m+n
                print(m)
            elif j==1:
                m=m-n
                print(m)
            elif j==2:
                m=m*n
                print(m)
            elif j==3:
                m=m//n
                print(m)
            
    



    
    