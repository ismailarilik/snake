#-*-coding=utf-8-*-

# ice aktarmalar
from Tkinter import Canvas, Frame

# yılanın hareket edeceği alanı sınırlayan duvarın sınıfı
class Duvar(object):
    def __init__(self, oyun, anaPencere):
        self.ilkBildirimYap(oyun)
        self.duvarGoster(anaPencere)
    
    
    
    # ilk bildirimler
    def ilkBildirimYap(self, oyun):
        
        self.oyun = oyun
        
        
        
        self.duvarBoyutlari = [32, 32]
        self.renk = "#00FF00"
    
    # duvarı ana pencerede göster
    def duvarGoster(self, anaPencere):
        # duvarın yerleşeceği çerçeveleri oluşturma
        self.yatayCerceve1 = Frame(anaPencere, width = self.duvarBoyutlari[0] * 10, height = 10)
        self.yatayCerceve1.place(x = 0, y = 0)
        
        self.yatayCerceve2 = Frame(anaPencere, width = self.duvarBoyutlari[0] * 10, height = 10)
        self.yatayCerceve2.place(x = 0, y = self.duvarBoyutlari[1] * 10 - 10)
        
        self.dikeyCerceve1 = Frame(anaPencere, width = 10, height = self.duvarBoyutlari[1] * 10)
        self.dikeyCerceve1.place(x = 0, y = 0)
        
        self.dikeyCerceve2 = Frame(anaPencere, width = 10, height = self.duvarBoyutlari[1] * 10)
        self.dikeyCerceve2.place(x = self.duvarBoyutlari[0] * 10 - 10, y = 0)
        
        
        
        ### "Canvas" ları oluşturma ve çerçevelere yerleştirme
        # Yatay duvarlar
        x = 0
        y = 0
        for i in range(self.duvarBoyutlari[0]):
            canvas = Canvas(self.yatayCerceve1, width = 10, height = 10,
                            bg = self.renk, highlightthickness = 0)
            canvas.place(x = x, y = y)
            canvas = Canvas(self.yatayCerceve2 ,width = 10, height = 10,
                            bg = self.renk, highlightthickness = 0)
            canvas.place(x = x, y = y)
            x += 10
        # Dikey duvarlar
        x = 0
        y = 0
        for i in range(self.duvarBoyutlari[1]):
            canvas = Canvas(self.dikeyCerceve1 ,width = 10, height = 10, bg = self.renk,
                            highlightthickness = 0)
            canvas.place(x = x, y = y)
            canvas = Canvas(self.dikeyCerceve2 ,width = 10, height = 10, bg = self.renk,
                            highlightthickness = 0)
            canvas.place(x = x, y = y)
            y += 10