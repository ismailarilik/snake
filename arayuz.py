#-*-coding=utf-8-*-

# içe aktarmalar
from Tkinter import Tk, Menu, Toplevel, Canvas, Label, Text, Button, END, mainloop, Frame
from functools import partial





# ana pencerenin sınıfı
class AnaPencere(Tk):
    def __init__(self, oyun, anaPencereGenislik = 320, anaPencereYukseklik = 320):
        Tk.__init__(self)
        self.ilkBildirimYap(oyun)
        self.anaPencereDuzenle(anaPencereGenislik, anaPencereYukseklik)
        self.anaPencereTusAyarla()
    
    
    # ilk bildirimleri yap
    def ilkBildirimYap(self, oyun):
        self.oyun = oyun
    
    
    # ana pencere oluştur
    # Pencere Olusturma
    def anaPencereDuzenle(self, anaPencereGenislik, anaPencereYukseklik):
        # ekran genisligi
        ekranGenislik = self.winfo_screenwidth()
        # ekran yuksekligi
        ekranYukseklik = self.winfo_screenheight()
        self.anaPencereGenislik = anaPencereGenislik    # pencere genisligi
        self.anaPencereYukseklik = anaPencereYukseklik    # pencere yuksekligi
        # pencereyi ortalamaya yarayacak x degeri
        self.anaPencereX = (ekranGenislik - self.anaPencereGenislik) / 2
        # pencereyi ortalamaya yarayacak y degeri
        self.anaPencereY = (ekranYukseklik - self.anaPencereYukseklik) / 2
        # pencerenin buyuklugunu ayarlama ve pencereyi ortalama
        self.geometry("%dx%d+%d+%d" %(self.anaPencereGenislik, self.anaPencereYukseklik,
                                                 self.anaPencereX, self.anaPencereY))
        # pencereyi güncelle
        self.update()
    
    
    # ana pencere etkinken görevlendirilecek tuşları ayarla ve görev ata
    def anaPencereTusAyarla(self):
        # birincil tuslar
        self.bind("<Return>", self.oyun.oyunuDuraklatYenidenBaslat)
        # ayarlar penceresi için tuş
        self.bind("<Control-c>", partial(AyarPen, self.oyun, self))
        # Çıkış için tuş
        self.bind("<Control-q>", partial(self.pencereCikis, self))
        # yeniden başlatmak için tuş
        self.bind("<Control-n>", self.oyun.oyunuYenidenBaslat)
        
        # ikincil tuslar
        self.bind("<space>", self.oyun.oyunuDuraklatYenidenBaslat)
        
        """self.bind("y", self.yemAyarla)"""
    
    """
    def yemAyarla(self, event = None):
        # yeni yem koyma
        self.oyun.yem.yeminYeriniAyarla(self.oyun.saha.sahaBoyutlari, [])
        
        # yemi goster
        self.oyun.yem.yemGoster(self.oyun.saha.canvasDizisiSaha)"""
    
    
    # pencereyi kapat
    def pencereCikis(self, pencere, event = None):
        pencere.destroy()





# menü sınıfı
class Menum(Menu):
    def __init__(self, oyun, anaPencere):
        Menu.__init__(self, anaPencere)
        self.ilkBildirimYap(oyun, anaPencere)
        self.menuOlustur()
    
    
    # ilk bildirimleri yap
    def ilkBildirimYap(self, oyun, anaPencere):
        self.oyun = oyun
        self.anaPencere = anaPencere
    
    
    # ana pencere üstündeki menüleri oluştur
    def menuOlustur(self):
        self.anaPencere.config(menu = self)
        self.dosya = Menu(self)
        self.add_cascade(label = "Oyun", menu = self.dosya)
        
        self.dosya.add_command(label = "Basla", command = self.oyun.oyunuDuraklatYenidenBaslat)
        self.dosya.add_command(label = "Yeniden Basla", command = self.oyun.oyunuYenidenBaslat)
        self.dosya.add_command(label = "Duraklat", command = self.oyun.oyunuDuraklatYenidenBaslat)
        self.dosya.add_command(label = "Ayarlari Yap", command = partial(AyarPen, self.oyun, self))
        self.dosya.add_command(label = "Cikis", command = self.anaPencere.quit)





class AyarPen(Toplevel):
    def __init__(self, oyun, anaPencere, event = None):
        Toplevel.__init__(self, anaPencere)
        self.ilkBildirimYap(oyun, anaPencere)
        self.ayarlarPenceresiAc()
    
    
    # ilk bildirimleri yap
    def ilkBildirimYap(self, oyun, anaPencere):
        self.oyun = oyun
        self.anaPencere = anaPencere
    
    
    # ayarların yapılabileceği pencereyi aç
    def ayarlarPenceresiAc(self, event = None):
        
        # acilir pencere yapimi
        # oyunun ayarlarini yapmak icin kullanilir.
        self.pencereTopGenislik = 300    # pencere genisligi
        self.pencereTopYukseklik = 350    # pencere yuksekligi
        # ekran genisligi
        self.ekranGenislik = self.anaPencere.winfo_screenwidth()
        # ekran yuksekligi
        self.ekranYukseklik = self.anaPencere.winfo_screenheight()
        # pencereyi ortalamaya yarayacak x degeri
        self.pencereTopX = (self.ekranGenislik - self.pencereTopGenislik) / 2
        # pencereyi ortalamaya yarayacak y degeri
        self.pencereTopY = (self.ekranYukseklik - self.pencereTopYukseklik) / 2
        self.geometry("%dx%d+%d+%d" %(self.pencereTopGenislik, self.pencereTopYukseklik,
                                                 self.pencereTopX, self.pencereTopY))
        self.transient(self.anaPencere)
        
        
        
        # Renk kodlarini tutan dizi...
        self.renkler = [["#FF0000", "#FFFF00", "#FFFFFF", "#000000",
                         "#19FF00", "#00FFFF", "#0000FF", "#FF00FF",
                         "#AA004C", "#7C0000", "#FF7700", "#7FFFD4",
                         "#FFE4C4", "#8B8B00", "#FF99FF", "#8A2BE2"],
                        ["#556B2F", "#B8C1FF", "#FFBCA5", "#8B0000",
                         "#2F4F4F", "#1C86EE", "#8B8386", "#E0FFFF",
                         "#87CEFA", "#BA55D3", "#3CB371", "#FFDEAD",
                         "#BBFFFF", "#8B7E66", "#8B3626", "#75511A"],
                        ["#8F6B32", "#E85752", "#F08682", "#9C0F56",
                         "#888A85", "#BABDB6", "#4D2600", "#803F00",
                         "#BF5E00", "#5A00B3", "#BFF500", "#BFF500",
                         "#00484D", "#006066", "#007880", "#00A7B3"],
                        ["#00B377", "#00CC88", "#8BB300", "#FF8080",
                         "#FFD9B0", "#C3B4DA", "#8B4726", "#888A85",
                         "#8E79A5", "#638000", "#00438A", "#644A9B",
                         "#8B4C39", "#FF8247", "#8B3626", "#8B636C"]]
        
        
        
        
        
        ### Renk seçme bölgelerini oluştur
        # etiketlerin "text" seçeneklerine atanacak karakter dizilerini tutan liste
        yaziEtiket = ["Yilanin rengi:", "Sahanin rengi:", "Duvarin rengi:", "Yemin rengi:"]
        # örnekleri bulunduran "Canvas" ların listesini taşıyan liste
        self.canvasDizDizOrnek = [[], [], [], []]
        # örnekler için öntanımlı renklerin kodlarını bulunduran liste
        renkOntanimli = ["#FFFFFF", "#FF0000", "#00FF00", "#0000FF"]
        for bolge in range(4):
            ## etiketleri oluştur
            etiket = Label(self, text = yaziEtiket[bolge])
            etiket.place(x = 0, y = bolge * 50)
            
            # etiketlerin altında bulunan ve örnek olan "Canvas" ları oluşturma ve listeye yazma
            sayac2 = 0
            for sayac in range(5):
                self.canvasDizDizOrnek[bolge].append(Canvas(self,
                                                            width = 10, height = 10,
                                                            bg = renkOntanimli[bolge]))
                self.canvasDizDizOrnek[bolge][sayac].place(x = sayac2, y = bolge * 50 + 20)
                sayac2 += 10
            
            # Renklerin seçilebildiği Canvas ları oluşturma ve görev atama
            for satir in range(4):
                sayac2 = 100
                for sayac in range(16):
                    canvas = Canvas(self, width = 10, height = 10,
                                    bg = self.renkler[satir][sayac])
                    canvas.place(x = sayac2, y = satir * 10 + bolge * 50)
                    canvas.bind("<Button-1>",
                            partial(self.oyun.canvasDizisiBoya, self.canvasDizDizOrnek[bolge], canvas["bg"]))
                    sayac2 += 10
        
        
        
        # Sahanin genisligi ve yuksekligi
        # etiketler
        self.etiket5 = Label(self, text = "Sahanin Genisligi:")
        self.etiket5.place(x = 0, y = 200)
        self.etiket6 = Label(self, text = "Sahanin Yuksekligi:")
        self.etiket6.place(x = 0, y = 240)
        self.etiket7 = Label(self, text = "Yilanin Hizi:")
        self.etiket7.place(x = 0, y = 280)
        # yazi kutulari
        self.yazi = Text(self, width = 5, height = 1, bg = "#FFFFFF")
        self.yazi.insert(END, "30")    # "Text" kutusuna ontanimli metin yerlestirme
        self.yazi.place(x = 130, y = 200)
        self.yazi2 = Text(self, width = 5, height = 1, bg = "#FFFFFF")
        self.yazi2.insert(END, "30")    # "Text" kutusuna ontanimli metin yerlestirme
        self.yazi2.place(x = 130, y = 240)
        self.yazi3 = Text(self, width = 5, height = 1, bg = "#FFFFFF")
        self.yazi3.insert(END, "15")    # "Text" kutusuna ontanimli metin yerlestirme
        self.yazi3.place(x = 130, y = 280)
        
        # "Tamam" dugmesi
        self.dugme = Button(self, width = 5, height = 1, text = "Tamam",
                            command = partial(self.oyun.yeniDegerlerleDuzenlemeyiCalistir,
                                              self.canvasDizDizOrnek, self.yazi, self.yazi2,
                                              self.yazi3, self))
        self.dugme.place(x = 130, y = 320)