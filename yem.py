#-*-coding=utf-8-*-

# ice aktarmalar
from random import randrange

# yilanin yiyecegi yemin sinifi
class Yem(object):
    def __init__(self, oyun, canvasDizisiSaha):
        self.ilkBildirimYap(oyun)
        self.yemGoster(canvasDizisiSaha)
    
    
    
    # İlk bildirimleri yap
    def ilkBildirimYap(self, oyun):
        
        self.oyun = oyun
        
        
        
        self.yemKoor = [5, 5]
        self.renk = "#0000FF"
    
    
    # yemi gosterme
    def yemGoster(self, canvasDizisiSaha):
        canvasDizisiSaha[self.yemKoor[0]][self.yemKoor[1]].configure(bg = self.renk)
    
    
    
    # yilanin yiyecegi yemin yerini belirleyen fonksiyon
    def yeminYeriniAyarla(self, sahaBoyutlari, yilanKoor):
        self.yemKoor[0] = randrange(sahaBoyutlari[1])
        self.yemKoor[1] = randrange(sahaBoyutlari[0])
        while self.yemKoor in yilanKoor:
            self.yemKoor[0] = randrange(sahaBoyutlari[1])
            self.yemKoor[1] = randrange(sahaBoyutlari[0])