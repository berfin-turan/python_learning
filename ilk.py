ad=input("Adınızı Girin: ")
soyad=input("Soyadınızı Girin: ")
yas=int(input("Yaşınızı Girin: "))

bilgiler=[ad,soyad,yas]

print("\n\nAd: {}  \nSoyad: {}  \nYaş: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))


if yas<18:
    print("\nYetişkin Değilsiniz.\n")
else:
    print("\nYetişkinsiniz.\n")