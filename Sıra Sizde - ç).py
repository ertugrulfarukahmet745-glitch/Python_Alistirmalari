vki=int(input("Kilonuzu Yazınız: "))
vki1=int(input("Boyunuzu Yazınız : "))
vki2=vki1/100
Vki=vki/(vki2*vki2)
if Vki<18:
    print("Zayıf")
elif Vki>=18 and Vki<25:
    print("Normal")
elif Vki>=25 and Vki<30:
    print("Kilolu")
elif Vki>=30 and Vki<35:
    print("Obez")
else:
    print("Ciddi Obez")
