def perkalian(a,b):
    hasil = (a * b)-a
    i = 0
    print(f'{a} x {b} = ', end='')
    while i < hasil  :
        print(b,'+', end=' ')
        i += a
    else:
        print(b, end='')
        print(' =',a*b)
    
        

perkalian(6,5)
perkalian(7,10)
