kitab={
    'ad': "kendine hosh geldin" ,
    'yazar': "mirach chagri aktash",
    'il': "2015" ,
    'sehife sayi': "200" 
}
a=[]
def Showbook():
    for key,val in kitab.items():
        print(key,": ",val)

Showbook()

def changebook():
    kitab["ad"]=input("kitabin adini deyish: ")
    for key,val in kitab.items():
        print(key,": ",val)
        break
    
changebook()