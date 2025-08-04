def menu_ekrani():
    print("-----Mini Atm-----")
    print("1.Bakiye Göster")
    print("2.Para Yatır")
    print("3.Para Çek")
    print("4.Çıkış")
    
def bakiye_goster(bakiye):
    print("Mevcut bakiyeniz: {} TL\n".format(bakiye))
    
def para_yatir(bakiye):
    
    yatirilacak=float(input("Yatırmak istediğiniz tutarı girin: "))
    
    if yatirilacak<=0:
        print("Geçersiz miktar!!")
    else:
        bakiye+=yatirilacak
        print("{} TL başarıyla yatırıldı.Toplam bakiye: {}\n".format(yatirilacak,bakiye))
    return bakiye

def para_cek(bakiye):
    
    cekilecek=float(input("Çekmek istediğiniz tutarı girin: "))

    if cekilecek<=0:
        print("Geçersiz miktar!!")
    elif cekilecek>bakiye:
        print("Yetersiz bakiye!!")
    else:
        bakiye-=cekilecek
        print("{} TL başarıyla çekildi.Kalan bakiye: {}\n".format(cekilecek,bakiye))
    return bakiye

def giris_ekrani():#Kullanıcı şifre kontrolü ile işlemlere erişim sağlar.
    dogru_sifre="BT123"
    hak=3
    
    while hak >0:
        
        sifre=input("Lütfen şifrenizi girin: ")
        if sifre==dogru_sifre:
            print("Giriş başarılı.\n")
            return True
        else:
            hak-=1
            print("Hatalı şifre.Kalan deneme hakkı: {}".format(hak))
    
    print("Çok fazla hatalı deneme.Hesap kilitlendi.")
    return False

bakiye=0.0

if giris_ekrani():#Şifre doğru ise işlemler yapılır.
    while True:
        menu_ekrani()
        secim=input("Bir işlem seçiniz: ")
        
        if secim=="1":
            bakiye_goster(bakiye)
        elif secim=="2":
            bakiye=para_yatir(bakiye)
        elif secim=="3":
            bakiye=para_cek(bakiye)
        elif secim=="4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Lütfen geçerli bir giriş yapın.\n")

    
