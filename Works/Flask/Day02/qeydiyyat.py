

class qeydiyyat():
    def __init__(self,ad,soyad,email,telefon, shifre):
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.telefon = telefon
        self.shifre = shifre

    def ad(self):
        self.ad=input(str("adinizi daxil edin: "))    
        if self.ad== "":
            return self.ad
        

    def soyad(self):
        self.soyad=input(str("soyadinizi daxil edin: "))
        if self.soyad=="":
            return self.soyad

    def email(self):
        self.email=input(str("emailinizi daxil edin: "))

    def telefon(self):
        self.telefon=input(str("telefon nomrenizi daxil edin: +994 " ))    
        if len(self.telefon)!=9:
            print("telefon nomresinin uzunlugu 9 olmalidir") 
        else:
            print("nomreni duzgun daxil edin")    

    def shifre(self):
        self.shifre=input(str("shifrenizi daxil edin: "))
        if len(self.shifre)<8:
            print("en azi 8 xarakter daxil etmelisiniz")
        if len(self.shifre)>15:
            print("max 15 xarakter daxil ede bilersiniz")    



goster=qeydiyyat()
goster.ad()
goster.soyad()
goster.email()
goster.telefon()
goster.shifre()
