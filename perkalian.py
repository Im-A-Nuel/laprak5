def perkalian(a,b):
    hsl=a*b
    print(a,'x',b,'=', end=' ')
    for i in range(1,a):
        print(b, end=' + ')
    print(b,'=',hsl)
    
        
perkalian(-5,6)
perkalian(7,10)
