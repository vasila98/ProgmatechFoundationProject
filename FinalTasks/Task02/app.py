Telebeler=["vesi","gunay"]
Giris_bali=[47,45]
Imtahan_bali=[47,45]

def TelebeniElaveEt():
    AdSoyad=input("Telebenin adini ve Soyadini daxil edin:")
    GirisBali=int(input("Telebenin giris balini qeyd edin:"))
    ImtahanBali=int(input("Telebenin imtahanda yigdigi bali qeyd edin:"))
    Telebeler.append(AdSoyad)
    Giris_bali.append(GirisBali)
    Imtahan_bali.append(ImtahanBali)
    print(" Telebe elave edildi")
    


def TelebeniSil():
    AdSoyad=input("Silinecek Ad ve Soyadi daxil edin:")
    if AdSoyad in Telebeler:
        SilinecekSn=Telebeler.index(AdSoyad)
        Telebeler.pop(SilinecekSn)
        Giris_bali.pop(SilinecekSn)
        Imtahan_bali.pop(SilinecekSn)

    else:
        print("Silmek istediyiniz telebe siyahida yoxdur.")    

    

def TelebeniAxtar():
    AdSoyad=input("Axtarilacaq Ad ve Soyadi daxil edin:")
    if AdSoyad in Telebeler:
        AxtarilanSn=Telebeler.index(AdSoyad)
        print(f"{'Ad Soyad':10} {'Giris Bali':10} {'Imtahan Bali':10} {'Umumi Bal':10} {'Netice':15}")

        Hesablama=Giris_bali[AxtarilanSn]+Imtahan_bali[AxtarilanSn]
        if Hesablama>=51 and Imtahan_bali[AxtarilanSn]>=17:
            Netice=" Imtahandan Kecdi"
        else: 
            Netice=" Imtahandan Kesildi"    
        print(f"{Telebeler[AxtarilanSn]:10} {Giris_bali[AxtarilanSn]:10} {Imtahan_bali[AxtarilanSn]:10} {Hesablama:10} {Netice:15}")

    else:
        print("Axtardiginiz telebe siyahida yoxdur.")    

    

def TelebeniGoster():
    print(f"{'Ad Soyad':10} {'Giris Bali':10} {'Imtahan Bali':10} {'Umumi Bal':10} {'Netice':15}")
    for sn in range(len(Telebeler)):
        Hesablama=Giris_bali[sn]+Imtahan_bali[sn]
        if Hesablama>=51 and Imtahan_bali[sn]>=17 :
            Netice=" Imtahandan Kecdi"
        else:
            Netice=" Imtahandan Kesildi"    
        print(f"{Telebeler[sn]:10} {Giris_bali[sn]:10} {Imtahan_bali[sn]:10} {Hesablama:10} {Netice:15}")
    

def TelebeleriYenile():
     AdSoyad=input("Axtarilacaq Ad ve Soyadi daxil edin:")
     if AdSoyad in Telebeler:
         AxtarilanSn=Telebeler.index(AdSoyad)
         print(f"{'Ad Soyad':10} {'Giris Bali':10} {'Imtahan Bali':10} {'Umumi Bal':10} {'Netice':15}")

         Hesablama=Giris_bali[AxtarilanSn]+Imtahan_bali[AxtarilanSn]
         if Hesablama>=51 and Imtahan_bali[AxtarilanSn]>=17:
             Netice=" Imtahandan Kecdi"
         else:
             Netice=" Imtahandan Kesildi"    
         print(f"{Telebeler[AxtarilanSn]:10} {Giris_bali[AxtarilanSn]:10} {Imtahan_bali[AxtarilanSn]:10} {Hesablama:10} {Netice:15}")

     YeniAdSoyad=input("Yeni ad ve soyadi daxil edin:") 
     YeniGirisBali=input("Yeni giris balini daxil edin:")
     YeniImtBali=input("Yeni imtahan balini daxil edin:")
     Telebeler[AxtarilanSn]=YeniAdSoyad
     Giris_bali[AxtarilanSn]=YeniGirisBali
     Imtahan_bali[AxtarilanSn]=YeniImtBali

 

def ImtKesilenleriGoster():
       print(f"{'Ad Soyad':10} {'Giris Bali':10} {'Imtahan Bali':10} {'Umumi Bal':10} {'Netice':15}")
       for sn in range(len(Telebeler)):
           Hesablama=Giris_bali[sn]+Imtahan_bali[sn]
           if Hesablama>51 and Imtahan_bali[sn]<17  :
               Netice="Imtahandan kesildi"
           elif Hesablama<51:
               Netice="Imtahandan kesildi"    
               print(f"{Telebeler[sn]:10} {Giris_bali[sn]:10} {Imtahan_bali[sn]:10} {Hesablama:10} {Netice:15}")
    

def ImtKecenleriGoster():
      print(f"{'Ad Soyad':10} {'Giris Bali':10} {'Imtahan Bali':10} {'Umumi Bal':10} {'Netice':15}")
      for sn in range(len(Telebeler)):
           Hesablama=Giris_bali[sn]+Imtahan_bali[sn]
           if Hesablama>=51 and Imtahan_bali[sn]>=17:
               Netice="Imtahandan kecdi"
               print(f"{Telebeler[sn]:10} {Giris_bali[sn]:10} {Imtahan_bali[sn]:10} {Hesablama:10} {Netice:15}")
    




def emeliyyatlar():
    FunksiyaSiyahisi=[TelebeniElaveEt,TelebeniSil,TelebeniAxtar,TelebeniGoster,TelebeleriYenile,ImtKesilenleriGoster,ImtKecenleriGoster]
    while True:

        print(""" 
         0. Proqramdan cix
         1. Telebeni elave et
         2. Telebeni sil
         3. Telebeni axtar
         4. Telebeleri goster
         5. Telebeleri yenile
         6. Imtahandan kesilen telebeleri goster
         7. Imtahandan kecen telebeleri goster
   
             """) 

        secim=int(input("Zehmet olmasa hansi emeliyyati yerine yetirmek isteyirsizse reqem secin (0-7):"))
        if secim<=7 and secim>=1:
            FunksiyaSiyahisi[secim-1]()
            print("\n"*5)
            print("Emeliyyatiniz yerine yetirilir")   
        elif secim==0:
            print("Proqramdan cixir")
            break
        else:
            print("Zehmet olmasa 0 ve 7 arasinda bir reqem secin!!!")   
        
     

emeliyyatlar()    
