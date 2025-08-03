
def toplama(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    if b==0:
        return "Sıfıra bölüm hatası!!!"
    else:
        return a/b
    
def factorial(sayi):
    faktöriyel=1
    if sayi<0:
        return "Negatif sayilarin faktöriyeli hesaplanamaz!!!"
    else:
        for i in range(1,sayi+1):
            faktöriyel*=i
        return faktöriyel

def fibonacci(sayi):
    x=0
    y=1
    if sayi<0:
        return "Lütfen geçerli bir sayi girin."
    else:
        fib_liste=[]
        for i in range(sayi):
            fib_liste.append(x)
            z=x+y
            x=y
            y=z
        return fib_liste
        
    
print("*****Matematik Menüsü*****\n")

while True:
    print("1.Toplama")
    print("2.Çıkarma")
    print("3.Çarpma")
    print("4.Bölme")
    print("5.Faktöriyel")
    print("6.Fibonacci")
    print("7.Çikiş\n")
    
    secim=int(input("Hangi işlemi yapmak istersiniz: "))
    
    if secim in [1,2,3,4,5,6]:
        if secim==1:
            toplam1=int(input("Birinci sayısı girin: "))
            toplam2=int(input("İkinci sayıyı girin: "))
            print("Toplama Sonucu: ",toplama(toplam1,toplam2),"\n")
        elif secim==2:
            cikarilan=int(input("Çıkarılan sayıyı girin: "))
            cikan=int(input("Çıkan sayıyı girin: "))
            print("Çıkarma Sonucu: ",cikarma(cikarilan,cikan),"\n")
        elif secim==3:
            carpim1=int(input("Birinci sayısı girin: "))
            carpim2=int(input("İkinci sayıyı girin: "))
            print("Çarpma Sonucu: ",carpma(carpim1,carpim2),"\n")
        elif secim==4:
            bolunen=int(input("Bölünen sayıyı girin: "))
            bolen=int(input("Bölen sayıyı girin: "))
            print("Bölme Sonucu: ",bolme(bolunen,bolen),"\n")
        elif secim==5:
            sayi=int(input("Faktöriyeli alınacak sayıyı girin: "))
            print("Faktöriyel Sonucu: ",factorial(sayi),"\n")
        else:
            sayi2=int(input("Fibonacci dizisinin kaç elemanını görmek istersiniz?: "))
            print("İstenilen dizi: ",fibonacci(sayi2),"\n")
               
    elif secim==7:
        print("Çikiş yapiliyor...\n\n")
        break
    else:
        print("Hatali seçim.Tekrar deneyin.\n")
    

    