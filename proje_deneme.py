import time
from idlelib.scrolledlist import ScrolledList

from kütüphane import *
print("""Kütüphane Programına Hoşgeldiniz

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil

5.Baskıyı Yükselt

Çıkmak İçin 'Çık' Yazınız

""")

kütüphane=Kütüphane()
while True:
    işlem=input("Yapacağınız İşlem: ")
    if (işlem == "Çık"):
        print("Program Kapanıyor")
        print("Yine Bekleriz")
        break
    elif (işlem=="1"):
        kütüphane.kitapları_goster()
    elif (işlem=="2"):
        isim=input("Hangi Kitabı İstiyorsunuz ? ")
        print("Kitap Aranıyor")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
    elif (işlem=="3"):
        isim=input("İsim: ")
        yazar=input("Yazar: ")
        yayınevi=input("Yayınevi: ")
        tür=input("Tür: ")
        baskı=int(input("Baskı: "))
        yeni_kitap=Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap Ekleniyor")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap Sisteme Eklendi")
    elif (işlem=="4"):
        isim=input("Hangi Kitabı Silmek İstiyorsunuz ? ")
        cevap=input("Emin Misiniz ? Son Kez Kontrol Ediniz (E/H)")
        if (cevap=="E"):
            print("Kitap Siliniyor")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap Sistemden Silindi")
    elif (işlem=="5"):
        isim = input("Hangi Kitabın Baskısını Yükseltmek İstiyorsunuz? ")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)
        başarılı = kütüphane.baskı_yükselt(isim)
        if not başarılı:
            continue
    else:
        print("Geçersiz İşlem")