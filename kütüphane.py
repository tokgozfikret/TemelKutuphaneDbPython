import sqlite3
import time

class Kitap():
    def __init__(self,isim,yazar,yayınevi,tür,baskı):
        self.isim=isim
        self.yazar=yazar
        self.yayınevi=yayınevi
        self.tür=tür
        self.baskı=baskı
    def __str__(self):
        return "Kitap İsmi: {}\nYazar:  {}\nYayınevi:  {}\nTür:  {}\nBaskı:  {}\n".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)
class Kütüphane():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("kütüphane.db")
        self.cursor=self.baglanti.cursor()
        sorgu="CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglantiyi_kes.close()
    def kitapları_goster(self):
        sorgu="Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar=self.cursor.fetchall()
        if (len(kitaplar)==0):
            print("Kütüphanede Kitap Bulunmuyor")
        else:
            for i in kitaplar:
                kitap=Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
    def kitap_sorgula(self,isim):
        sorgu="Select * From kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if (len(kitaplar)==0):
            print("Böyle Bir Kitap Bulunmuyor")
        else:
            kitap=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)
    def kitap_ekle(self,kitap):
        sorgu="Insert into kitaplar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))
        self.baglanti.commit()
    def kitap_sil(self,isim):
        sorgu="Delete From kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def baskı_yükselt(self, isim):
        sorgu = "Select * From kitaplar where isim=?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Bu Kitap Kütüphanede Bulunmuyor. Lütfen Tekrar Deneyiniz.")
            return False
        mevcut_baskı = kitaplar[0][4]
        print(f"Kitabın Mevcut Baskısı: {mevcut_baskı}")
        yeni_baskı = int(input("Kaçıncı Baskıya Yükseltmek İstiyorsunuz? "))
        sorgu2 = "Update kitaplar set baskı =? where isim =?"
        self.cursor.execute(sorgu2, (yeni_baskı, isim))
        self.baglanti.commit()
        print(f"Kitap Başarıyla {yeni_baskı}. Baskıya Yükseltildi.")
        return True


