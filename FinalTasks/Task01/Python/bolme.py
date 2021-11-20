# iki eded daxil etmek lazimdi, // secende neticeni floatla versin, / secende tam versin


def tamBol (a,b):
    print(int(a/b))

def kesrleBol(a,b):
    print(float(a//b))   

x=int(input('birinci ededi daxil edin :'))    
y=int(input('ikinci ededi daxil edin :'))
emr=input('emr(//,/ isarelerinden birini daxil et):')

if emr=='/':
    tamBol(x,y)

if emr=='//':
    kesrleBol(x,y)