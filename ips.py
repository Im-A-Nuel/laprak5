def ips(matkul):
    poin=0
    i=1
    while (i<=matkul):
        nilai=str(input(f'Nilai MK:{i}:'))
        i=i+1
    if nilai=='A':
        poin_=+4
    elif nilai=='B':
        poin_=+3
    elif nilai=='D':
        poin_=+2
    elif nilai=='E':
        poin_=+1
    poin=poin+poin_
 
    IPS = (poin*3)/(matkul/3)
    
    print(f'Nilai IPS anda semester ini {IPS}')
        

matkul=int(input('Berapa jumlah mata kuliah?'))
ips(matkul)
