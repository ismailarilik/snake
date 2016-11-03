#-*-coding=utf-8-*-

# içe aktarmalar
from Tkinter import Text, Frame, Scrollbar, END

# oyunla ilgili gösterilecek bilgilerin sınıfının tanımı
class Bilgi(object):
    
    def __init__(self, oyun, anaPencere):
        self.ilkBildirimYap(oyun)
        # bilgi kutusuna yer hazırlamak için ana pencereyi büyüt ve ekranda ortala
        self.anaPencereBuyutYerlestir(anaPencere)
        # ana pencerede bilgilerin gösterileceği "Text" aracının konumlandırılacağı bir "Frame" oluştur
        self.cerceveOlustur(anaPencere)
        # çerçevenin üstünde bir yazı kutusu oluştur
        self.yaziKutusuOlusturAyarla()
    
    
    
    # ilk bildirimleri yap
    def ilkBildirimYap(self, oyun):
        
        self.oyun = oyun
        
        self.bilgi = ""
        
        self.bilgiKutusuYukseklik = 50
    
    
    
    # bilgi kutusuna yer hazırlamak için ana pencereyi büyüt ve ekranda ortala
    def anaPencereBuyutYerlestir(self, anaPencere):
        # pencerenin büyüklüğünü ve yerini öğren
        koorXAnaPencere = anaPencere.winfo_x()
        koorYAnaPencere = anaPencere.winfo_y()
        genislikAnaPencere = anaPencere.winfo_width()
        yukseklikAnaPencere = anaPencere.winfo_height()
        
        # pencerenin yeni büyüklüğünü ve yeni koordinatlarını belirle
        yukseklikAnaPencere += self.bilgiKutusuYukseklik
        koorYAnaPencere -= self.bilgiKutusuYukseklik / 2
        
        # pencereyi yeniden boyutlandır ve ekranda ortala
        anaPencere.geometry("%dx%d+%d+%d" %(genislikAnaPencere, yukseklikAnaPencere,
                                            koorXAnaPencere, koorYAnaPencere))
        
        # pencereyi güncelle
        anaPencere.update()
    
    
    
    # ana pencerede bilgilerin gösterileceği "Text" aracının konumlandırılacağı bir "Frame" oluştur
    def cerceveOlustur(self, anaPencere):
        # pencerenin büyüklüğünü ve yerini öğren
        koorXAnaPencere = anaPencere.winfo_x()
        koorYAnaPencere = anaPencere.winfo_y()
        genislikAnaPencere = anaPencere.winfo_width()
        yukseklikAnaPencere = anaPencere.winfo_height()
        
        # çerçevenin koordinatlarını ve büyüklüğünü ayarla
        koorXCerceve = 0
        koorYCerceve = yukseklikAnaPencere - self.bilgiKutusuYukseklik
        genislikCerceve = genislikAnaPencere
        yukseklikCerceve = self.bilgiKutusuYukseklik
        
        self.cerceve = Frame(anaPencere, width = genislikCerceve, height = yukseklikCerceve)
        self.cerceve.place(x = koorXCerceve, y = koorYCerceve)
    
    
    
    # çerçevenin üstünde bir yazı kutusu oluştur ve ayarlarını yap
    def yaziKutusuOlusturAyarla(self):
        
        # yazı kutusu oluştur
        self.yaziKutusu = Text(self.cerceve, bg = "#FFFFFF")
        #self.yaziKutusu.pack()
        self.yaziKutusu.place(x = 0, y = 0, relwidth = 1.0, relheight = 1.0)
        
        
        # yazı kutusu için kaydırma çubuğu oluştur ve ayarları yap
        kaydirmaCubugu = Scrollbar(self.cerceve)
        #kaydirmaCubugu.pack(side = RIGHT, fill = Y)
        kaydirmaCubugu.place(relx = 0.95, rely = 0, relheight = 1.0)
        
        self.yaziKutusu.config(yscrollcommand = kaydirmaCubugu.set)
        
        kaydirmaCubugu.config(command = self.yaziKutusu.yview)
    
    
    
    # Oyunla ilgili gönderilen bilgileri al ve kaydet
    def bilgiAl(self, bilgi):
        self.bilgi = bilgi
    
    
    
    # kaydedilen bilgileri göster
    def bilgiGoster(self):
        # yazı kutusuna bilgiyi ekle
        self.yaziKutusu.insert(END, "\n")
        self.yaziKutusu.insert(END, self.bilgi)
        
        # yazı kutusunun sonuna girilen yazının görünmesini sağla
        self.yaziKutusu.see(END)