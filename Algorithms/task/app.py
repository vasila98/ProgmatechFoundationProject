users=[]

def createUser():
    ad=input('istifadeci adi:')
    soyad=input('istifadeci soyadi:')
    email=input('istifadeci emaili:')

    user={
        'ad':ad
        'soyad':soyad
        'email':email
    }
    users.append(user)

def showAllUsers():

    for user in users:
        print(f'{ user ["ad]}')

createUser()
showAllUsers()        
