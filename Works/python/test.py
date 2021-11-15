adlar=[
    'Fezail',
    'Rehman',
    'Elmar',
    'Sebuhi',
    'Aysel',
    'Murad',
    'Vesile',
    'Ravi'
]

def adlariGoster():
    for i in range (len(adlar)):
        print(i,adlar[i])


def cutYerdekiler():
    for i in range (len(adlar)):
        i%2==0:
             print(i,adlar[i])


def listiSirala():
    adlar.sort()
    adlariGoster()



def daxilindeEherfiOlaniTap():
    for i in range(len(adlar)):
        if ad.find('e')!= -1:
            print(f'{ad} sozunde e herfi var')
        elif ad.find('E')!= -1:
            print(f'{ad} sozunde E herfi var')
        else :
            print(f'{ad} sozunde e herfi yoxdur')  

 daxilindeEherfiOlaniTap()



def sonHerfiiOlaniTap():
    for ad in adlar:
        if ad.find('i',-1)!=-1:
            print(ad)

sonHerfiiOlaniTap()



    

