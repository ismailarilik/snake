#-*-coding=utf-8-*-

# içe aktarmalar
from Tkinter import *





# oyunla ilgili gösterilecek bilgilerin yer alacağı alanın sınıfı
class BilgiKutusu(Text):
    def __init__(self, oyun, anaPencere):
        self.ilkBildirimYap(oyun, anaPencere)
        self.anaPencereBuyutYerlestir()
        Text.__init__(self, anaPencere, bg = "#FFFFFF")
        self.kaydirmaOlustur()
    
    
    # ilk bildirimleri yap
    def ilkBildirimYap(self, oyun, anaPencere):
        self.oyun = oyun
        self.anaPencere = anaPencere
        self.bilgiKutusuGenislik = self.anaPencere.winfo_width()
        self.bilgiKutusuYukseklik = 50
    
    
    # bilgi kutusuna yer hazırlamak için ana pencereyi büyüt ve ekranda ortala
    def anaPencereBuyutYerlestir(self):
        # pencerenin büyüklüğünü ve yerini öğren
        koorXAnaPencere = self.anaPencere.winfo_x()
        koorYAnaPencere = self.anaPencere.winfo_y()
        genislikAnaPencere = self.anaPencere.winfo_width()
        yukseklikAnaPencere = self.anaPencere.winfo_height()
        
        # pencerenin yeni büyüklüğünü ve yeni koordinatlarını belirle
        yukseklikAnaPencere += self.bilgiKutusuYukseklik
        koorYAnaPencere -= self.bilgiKutusuYukseklik / 2
        
        # pencereyi yeniden boyutlandır ve ekranda ortala
        self.anaPencere.geometry("%dx%d+%d+%d" %(genislikAnaPencere, yukseklikAnaPencere,
                                            koorXAnaPencere, koorYAnaPencere))
        
        # pencereyi güncelle
        self.anaPencere.update()
    
    
    # kaydırma çubuğu oluştur, ayarları yap ve taşıyıcıya yerleştir
    def kaydirmaOlustur(self):
        # yazı kutusu için kaydırma çubuğu oluştur ve ayarları yap
        kaydirmaCubugu = Scrollbar(self)
        #kaydirmaCubugu.pack(side = RIGHT, fill = Y)
        kaydirmaCubugu.place(relx = 0.97, relheight = 1.0)
        
        self.config(yscrollcommand = kaydirmaCubugu.set)
        
        kaydirmaCubugu.config(command = self.yview)





# oyunla ilgili gösterilecek bilgilerin sınıfının tanımı
class Bilgi(object):
    
    def __init__(self, oyun, bilgiKutusu):
        self.ilkBildirimYap(oyun, bilgiKutusu)
    
    
    
    # ilk bildirimleri yap
    def ilkBildirimYap(self, oyun, bilgiKutusu):
        self.oyun = oyun
        self.bilgiKutusu = bilgiKutusu
        self.bilgi = ""
    
    
    
    # Oyunla ilgili gönderilen bilgileri al ve kaydet
    def bilgiAl(self, bilgi):
        self.bilgi = bilgi
    
    
    
    # kaydedilen bilgileri göster
    def bilgiGoster(self):
        # yazı kutusuna bilgiyi ekle
        self.bilgiKutusu.insert(END, "\n")
        self.bilgiKutusu.insert(END, self.bilgi)
        
        # yazı kutusunun sonuna girilen yazının görünmesini sağla
        self.bilgiKutusu.see(END)