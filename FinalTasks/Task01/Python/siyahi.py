#siyahilarda bu emrleri yerine yetirmek lazimdir: 
#1.insert; 2.remove; 3.append; 4.sort; 5.pop; 6.reverse

#istenilen indekse elave etmek
list=["vesi","rehman","ravi"]
list.insert(1, "aysel")
print(list)

#siyahinin sonuna elave etmek
list=["fezail","sebuhi","elmar"]
list.append("murad")
print(list)

#istenilen sozu cixarmaq
list=["rehman","ravi", "elmar", "sebuhi", "vesi", "aysel", "murad", "fezail", "yusif"]
list.remove("yusif")
print(list)

#istenilen indeksdeki sozu cixarmaq
list=["rehman","ravi", "elmar", "sebuhi", "vesi", "aysel", "murad", "fezail", "yusif"]
list.pop(8)
print(list)

#siyahini tersine cevirmek
list=["rehman","ravi", "elmar", "sebuhi", "vesi", "aysel", "murad", "fezail"]
list.reverse()
print(list)

#siyahini ceshidlemek
list=["rehman","ravi", "elmar", "sebuhi", "vesi", "aysel", "murad", "fezail"]
list.sort()
print(list)
