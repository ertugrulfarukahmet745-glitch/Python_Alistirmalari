a=int(input("Üçgenin Birinci Kenarının Uzunluğunu Yazınız. "))
b=int(input("Üçgenin İkinci Kenarının Uzunluğunu Yazınız. "))
c=int(input("Üçgenin Üçüncü Kenarının Uzunluğunu Yazınız. "))
if a==b and a==c and b==c:
    print("Bu Bir Eşkenar Üçgen")
elif a==b or a==c or b==c:
    print("Bu Bir İkizkenar Üçgen")
else:
    print("Bu Bir Çeşitkenar Üçgen")
