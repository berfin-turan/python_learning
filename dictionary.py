
def kelime_cevir(sozluk):
    if not sozluk:
        print("Sözlük boş!")
    else:
        kelime=input("Çevirmek istediğiniz ingilizce kelimeyi girin: ").strip().lower()
        if kelime in sozluk:
            print(kelime+" : "+sozluk[kelime])
        else:
            print("Bu kelime sözlükte yok.")
        
def yeni_kelime_ekle(sozluk):
    kelime=input("Eklemek istediğiniz ingilizce kelimeyi girin: ").lower()
    if kelime in sozluk:
        print("Bu kelime zaten sözlükte var.")
    else:
        turkce=input("Kelimenin Türkçesini girin: ")
        sozluk[kelime]=turkce
        print("Kelime eklendi.")

def kelime_sil(sozluk):
    
    if not sozluk:
        print("Sözlük boş!")
    else:
        silinecek=input("Silmek istediğiniz kelimeyi girin: ").lower()
        
        if silinecek in sozluk:
            del sozluk[silinecek]
            print("Kelime silindi.")
        else:
            print("Bu kelime sözlükte yok!")
        
def listele(sozluk):
    
    if not sozluk:
        print("Sözlük boş.")
    else:
        print("\nSözlüğünüzdeki Kelimeler:\n")
    
        for ingilizce,turkce in sozluk.items():
            print(ingilizce+" : "+turkce)
            
    
sozluk={}

while True:
    print("\n***İngilizce-Türkçe Sözlük***\n")
    print("1.Kelime çevir.\n2.Yeni kelime ekle.\n3.Kelime sil.\n4.Tüm kelimeleri listele.\n5.Çıkış\n")
    
    secim=input("Yapmak istediğiniz işlemi seçin: ").strip()
    
    if secim=="1":
        kelime_cevir(sozluk)
    elif secim=="2":
        yeni_kelime_ekle(sozluk)
    elif secim=="3":
        kelime_sil(sozluk)
    elif secim=="4":
        listele(sozluk)
    elif secim=="5":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Lütfen geçerli bir giriş yapın!")
    
        