# iki eded daxil etmek lazimdi. ededlerin cemini, ferqini, hasilini cap eden funksiya yazmaq lazim

def topla(a,b):
    print(a+b)


def cix(a,b):
    print(a-b)


def vur(a,b):
    print(a*b)


x=int(input('birinci eded: '))      
y=int(input('ikinci eded: '))  
emr=input('emr(+,-,* isarelerinden birini daxil et) :')

if emr=='+':
    topla(x,y)

if emr=='-':
    cix(x,y)

if emr=='*':
    vur(x,y)            
