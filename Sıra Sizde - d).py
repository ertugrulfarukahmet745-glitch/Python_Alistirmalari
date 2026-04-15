a=input("Adınız: ")
b=int(input("Maaşınız: "))
c=int(input("Çalışma Süreniz (YIL): "))
if c>=11:
    d=b*(5/4)
    print(f"Sayın {a}, Zamlı Maaşınız {d}TL")
else:
    f=b*(115/100)
    print(f"Sayın {a}, Zamlı Maaşınız {f}TL")
