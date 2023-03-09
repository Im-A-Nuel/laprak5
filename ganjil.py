def barisan(bawah,atas):
    print(f'bawah = {bawah}, atas = {atas} adalah ', end=' ')
    if bawah<atas:
        for i in range(bawah, atas-1):
            if i%2!=0:
                print(i,end=',')
        print(atas-1,end='.')
    else:
        for i in range(bawah,atas+1,-1):
            if i%2!=0:
                print(i, end=',')
        print(atas+1,end='.')
                
barisan(97,82)                 
            
