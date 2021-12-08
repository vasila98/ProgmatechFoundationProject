print(" Reqemi texmin etme oyunu")

reqem=15

oyuncuReqemi=int(input("0 ve 30 arasinda bir reqem secin: "))

shans=3

while True:
    if shans !=0:
        if oyuncuReqemi>reqem:
            shans -=1
            print(shans, "shansiniz qaldi")
            oyuncuReqemi=int(input("Yaxsi fikirlesin bir daha secin :"))
        elif oyuncuReqemi<reqem:
            shans-=1
            print(shans, "shansiniz qaldi")
            oyuncuReqemi=int(input("Telesmeyin, fikirlesib secin:"))
        if oyuncuReqemi==reqem:
            print("Tebrik edirem  reqemi duzgun texmin etdiniz")   
            break     

    if shans==0:
        print("sizin shansiniz bitdi sagolun")
        break        