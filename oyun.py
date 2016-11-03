#!/usr/bin/env python
#-*-coding=utf-8-*-

# içe aktarmalar
from Tkinter import *
from arayuz import *
from cevre import *
from canli import *
from diger import *





# oyunun yöneticisi olan "Oyun" sınıfını tanımlama
class Oyun(object):
    def __init__(self):
        self.ilkBildirimYap()
        self.nesneOlustur()
        self.basla()
        self.anaPencere.mainloop()
    
    
    
    # İlk bildirimleri ve atamaları yap
    def ilkBildirimYap(self):
        self.oyunSuruyorMu = True
    
    
    
    # nesneleri oluştur
    def nesneOlustur(self):
        ### nesneleri oluştur ve böylece ilgili bağımsız ilk bildirimleri yap
        # ana pencereyi oluştur
        self.anaPencere = AnaPencere(self, 320, 320)
        
        # ÜST KISIM
        # üst duvarı oluştur ve yerleştir
        self.duvarUst = Duvar(self, self.anaPencere, 32, 1, "#00FF00")
        self.duvarUst.pack()
        # ORTA KISIM
        self.cerceveOrta = Frame(self.anaPencere)
        self.cerceveOrta.pack()
        # sol duvarı oluştur ve yerleştir
        self.duvarSol = Duvar(self, self.cerceveOrta, 1, 30, "#00FF00")
        self.duvarSol.pack(side = "left")
        # sahayı oluştur ve yerleştir
        self.saha = Saha(self, self.cerceveOrta)
        self.saha.pack(side = "left")
        # sağ duvarı oluştur ve yerleştir
        self.duvarSag = Duvar(self, self.cerceveOrta, 1, 30, "#00FF00")
        self.duvarSag.pack(side = "left")
        # ALT KISIM
        # alt duvarı oluştur ve yerleştir
        self.duvarAlt = Duvar(self, self.anaPencere, 32, 1, "#00FF00")
        self.duvarAlt.pack()
        # menüyü oluştur
        self.menu = Menum(self, self.anaPencere)
        
        # yılanı oluştur
        self.yilan = Yilan(self, self.anaPencere, self.saha.canvasDizisiSaha, self.saha.sahaRengi,
                                   sagYonTusu = "<Right>", asagiYonTusu = "<Down>",
                                   solYonTusu = "<Left>", yukariYonTusu = "<Up>",
                                   renk = "#FFFF00", beklemeSuresi = 0.05)
        # yemi oluştur
        self.yem = Yem(self, self.saha.canvasDizisiSaha)
        
        # oyunla ilgili bilgilerin gösterileceği yazı kutusunu oluştur ve yerleştir
        self.bilgiKutusu = BilgiKutusu(self, self.anaPencere)
        self.bilgiKutusu.pack()
        # bilgi kutusuna bilgileri yazdırmaya yarayacak nesneyi oluştur
        self.bilgi = Bilgi(self, self.bilgiKutusu)
    
    
    
    def basla(self, event = None):
        # yılanı başlat
        self.yilan.start()
    
    
    
    # girilen argumanlarla oyunu calistirir
    # daha sonra pencereyi kapatır
    def oyunuYenidenDuzenle(self, yilanRenk, sahaRenk, duvarRenk, yemRenk,
                            sahaGenislik, sahaYukseklik, yilanHizi, ayarPen):
        yilanRengi = yilanRenk
        sahaninRengi = sahaRenk
        duvarinRengi = duvarRenk
        yeminRengi = yemRenk
        sahaninBoyutuX = sahaGenislik
        sahaninBoyutuY = sahaYukseklik
        duvarinBoyutuX = sahaGenislik + 2
        duvarinBoyutuY = sahaYukseklik + 2
        beklemeSuresi = 1.0 / yilanHizi
        
        
        # ana pencereyi sahanin boyutuna gore yeniden boyutlandir
        anaPencereGenislik = duvarinBoyutuX * 10    # pencere genisligi
        anaPencereYukseklik = duvarinBoyutuY * 10    # pencere yuksekligi
        # ekran genisligi
        ekranGenislik = self.anaPencere.winfo_screenwidth()
        # ekran yuksekligi
        ekranYukseklik = self.anaPencere.winfo_screenheight()
        # pencereyi ortalamaya yarayacak x degeri
        anaPencereX = (ekranGenislik - anaPencereGenislik) / 2
        # pencereyi ortalamaya yarayacak y degeri
        anaPencereY = (ekranYukseklik - anaPencereYukseklik) / 2
        # pencerenin boyutunu ve ekrandaki yerini ayarlama
        self.anaPencere.geometry("%dx%d+%d+%d" %(anaPencereGenislik,
                                                        anaPencereYukseklik,
                                                        anaPencereX, anaPencereY))
        # pencereyi güncelle
        self.anaPencere.update()
        
        
        # Yeni bilgilere göre ayarları değiştirme
        self.saha.sahaBoyutlari[0] = sahaninBoyutuX
        self.saha.sahaBoyutlari[1] = sahaninBoyutuY
        self.saha.sahaRengi = sahaninRengi
        self.saha.sahaGoster(self.anaPencere)
        self.duvar.duvarBoyutlari[0] = duvarinBoyutuX
        self.duvar.duvarBoyutlari[1] = duvarinBoyutuY
        self.duvar.renk = duvarinRengi
        self.duvar.duvarGoster()
        self.yilan.renk = yilanRengi
        self.yilan.beklemeSuresi = beklemeSuresi
        self.yilan.yilanGoster(self.saha.canvasDizisiSaha, self.saha.sahaRengi)
        self.yem.renk = yeminRengi
        self.yem.yemGoster(self.saha.canvasDizisiSaha)
        
        
        ### bilgi kutusu ayarları
        # bilgi kutusuna yer hazırlamak için ana pencereyi büyüt ve ekranda ortala
        self.bilgi.anaPencereBuyutYerlestir(self.anaPencere)
        
        # ana pencerede bilgilerin gösterileceği "Text" aracının konumlandırılacağı bir "Frame" oluştur
        self.bilgi.cerceveOlustur(self.anaPencere)
        
        # çerçevenin üstünde bir yazı kutusu oluştur
        self.bilgi.yaziKutusuOlusturAyarla()
        
        
        # ayarlar penceresini kapat
        ayarPen.destroy()
    
    
    
    def oyunuYenidenBaslat(self, event = None):
        self.anaPencere.destroy()
        self.__init__()
    
    
    
    def oyunuDuraklatYenidenBaslat(self, event = None):
        # oyun sürüyorsa duraklat
        # durmuşsa devam ettir
        # ayrıca durma veya devam etme bilgisini göster
        if self.oyunSuruyorMu == True:
            self.yilan.yilaniDuraklatDevamEttir()
            self.oyunSuruyorMu = False
            self.bilgi.bilgiAl("Oyun duraklatildi.\nDevam etmek icin baslatma tusuna basin.")
            self.bilgi.bilgiGoster()
        elif self.oyunSuruyorMu == False:
            self.yilan.yilaniDuraklatDevamEttir()
            self.oyunSuruyorMu = True
            self.bilgi.bilgiAl("Oyun devam ediyor.\nDuraklatmak icin baslatma tusuna basin.")
            self.bilgi.bilgiGoster()
    
    
    # tek belirtecli bir "Canvas()" dizisi ve renk kodu alir ve "Canvas()" lari belirtilen renge boyar.
    def canvasDizisiBoya(self, canvasDizisi, renk, event = None):
        for canvas in canvasDizisi:
            canvas.configure(bg = renk)
    
    
    
    def yeniDegerlerleDuzenlemeyiCalistir(self, canvasDizDizOrnek, yazi, yazi2, yazi3,
                                               ayarPen):
        yilanRenk = canvasDizDizOrnek[0][0]["bg"]
        sahaRenk = canvasDizDizOrnek[1][0]["bg"]
        duvarRenk = canvasDizDizOrnek[2][0]["bg"]
        yemRenk = canvasDizDizOrnek[3][0]["bg"]
        sahaGenislik = int(yazi.get(1.0, END))
        sahaYukseklik = int(yazi2.get(1.0, END))
        yilanHizi = int(yazi3.get(1.0, END))
        
        self.oyunuYenidenDuzenle(yilanRenk, sahaRenk, duvarRenk, yemRenk,
                                 sahaGenislik, sahaYukseklik, yilanHizi, ayarPen)

    
    
    
    





if __name__ == "__main__":
    oyun = Oyun()