#-*-coding=utf-8-*-

# içe aktarmalar
from Tkinter import Frame, Canvas





# yılanın hareket edeceği sahanın sınıfı
class Saha(Frame):
    def __init__(self, oyun, anaPencere):
        Frame.__init__(self, anaPencere)
        self.ilkBildirimYap(oyun)
        self.sahaDuzenle()
        self.sahaGoster(anaPencere)
    
    
    # ilk bildirimleri yap
    def ilkBildirimYap(self, oyun):
        self.oyun = oyun
        # yilanin gezinecegi sahanin genisligi ve yuksekligi...
        self.sahaBoyutlari = [30, 30]    # ilki genislik(x), ikincisi yukseklik(y)
        self.sahaRengi = "#FF0000"    # sahanın rengi
    
    
    # sahanin ozelliklerini duzenle
    def sahaDuzenle(self):
        self.config(width = self.sahaBoyutlari[0] * 10, height = self.sahaBoyutlari[1] * 10)
    
    
    # sahayı göster
    def sahaGoster(self, anaPencere):
        # "Canvas" lari tutacak diziyi olusturma ve iclerine "Canvas" lari atama
        self.canvasDizisiSaha = []
        for i in range(self.sahaBoyutlari[1]):
            self.canvasDizisiSaha.append([])
        for i in range(self.sahaBoyutlari[1]):
            for j in range(self.sahaBoyutlari[0]):
                self.canvasDizisiSaha[i].append(Canvas(self, height = 10, width = 10,
                                                       bg = self.sahaRengi, highlightthickness = 0))
        
        # "Canvas" ları çerçeveye yerleştirme
        x = 0
        y = 0
        for dizi in self.canvasDizisiSaha:
            for canvas in dizi:
                canvas.place(x = x, y = y)
                x += 10
            x = 0
            y += 10





# yılanın hareket edeceği alanı sınırlayan duvarın sınıfı
class Duvar(Frame):
    def __init__(self, oyun, anaPencere, gen, yuk, renk):
        self.ilkBildirimYap(oyun, anaPencere, gen, yuk, renk)
        Frame.__init__(self, anaPencere, width = self.gen * 10, height = self.yuk * 10)
        self.canvasYerlestir()
    
    
    # ilk bildirimleri yap
    def ilkBildirimYap(self, oyun, anaPencere, gen, yuk, renk):
        self.oyun = oyun
        self.anaPencere = anaPencere
        self.gen = gen
        self.yuk = yuk
        self.renk = renk
    
    
    # canvas ları yerleştir
    def canvasYerlestir(self):
        x = 0
        y = 0
        for i in range(self.yuk):
            x = 0
            for j in range(self.gen):
                canvas = Canvas(self, width = 10, height = 10,
                                bg = self.renk, highlightthickness = 0)
                canvas.place(x = x, y = y)
                x += 10
            y += 10