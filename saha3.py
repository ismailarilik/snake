#-*-coding=utf-8-*-

# ice aktarmalar
from Tkinter import Canvas, Frame

class Saha(object):
    def __init__(self, oyun, anaPencere):
        self.ilkBildirimYap(oyun)
        self.sahaGoster(anaPencere)
    
    
    
    # İlk bildirimleri yap
    def ilkBildirimYap(self, oyun):
        
        # İlk bildirimler
        self.oyun = oyun
        # yilanin gezinecegi sahanin genisligi ve yuksekligi...
        self.sahaBoyutlari = [30, 30]    # ilki genislik(x), ikincisi yukseklik(y)
        self.sahaRengi = "#FF0000"    # sahanın rengi
    
    
    
    def sahaGoster(self, anaPencere):
        # sahanın yerleşeceği çerçeveyi oluştur
        self.cerceve = Frame(anaPencere, width = self.sahaBoyutlari[0] * 10,
                             height = self.sahaBoyutlari[1] * 10)
        self.cerceve.place(x = 10, y = 10)
        
        
        # "Canvas" lari tutacak diziyi olusturma ve iclerine "Canvas" lari atama
        self.canvasDizisiSaha = []
        for i in range(self.sahaBoyutlari[1]):
            self.canvasDizisiSaha.append([])
        for i in range(self.sahaBoyutlari[1]):
            for j in range(self.sahaBoyutlari[0]):
                self.canvasDizisiSaha[i].append(Canvas(self.cerceve, height = 10, width = 10,
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