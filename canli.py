#-*-coding=utf-8-*-

# içe aktarmalar
from time import sleep
from threading import Thread
from random import randrange





# Aciklamalar:
#
#    1.
#        Yon 1 = Sag
#        Yon 2 = Asagi
#        Yon 3 = Sol
#        Yon 4 = Yukari
#    2.
#        "koordinatlarim" dizisinde yilanin basi en basta olacak sekilde koordinatlar belirlenir.



class Yilan(Thread):
    def __init__(self, oyun, anaPencere, canvasDizisiSaha, sahaRengi,
                 sagYonTusu = None, asagiYonTusu = None,
                 solYonTusu = None, yukariYonTusu = None,
                 renk = "#FFFFFF", beklemeSuresi = 0.05):
        
        Thread.__init__(self)
        self.ilkBildirimYap(oyun, renk, beklemeSuresi)
        self.yilanGoster(canvasDizisiSaha, sahaRengi)
        if sagYonTusu and asagiYonTusu and solYonTusu and yukariYonTusu:
            self.tusAyarla(anaPencere, sagYonTusu, asagiYonTusu, solYonTusu, yukariYonTusu)
    
    
    
    # İlk bildirimleri yap
    def ilkBildirimYap(self, oyun, renk, beklemeSuresi):
        
        self.oyun = oyun
        self.yilanYasiyorMu = True
        self.yilanHareketEdiyorMu = True
        
        
        
        # ontanimli koordinatlar (bkz. madde 2)
        self.koordinatlarim = [[0, 3], [0, 2], [0, 1]]
        # yilanin bir onceki koordinatlarini tutar
        self.oncekiKoordinatlarim = [[0, 2], [0, 1], [0, 0]]
        self.yon = 1    # ontanimli yon
        self.renk = renk
        self.beklemeSuresi = beklemeSuresi
    
    
    
    def tusAyarla(self, anaPencere, sagYonTusu, asagiYonTusu, solYonTusu, yukariYonTusu):
        anaPencere.bind(sagYonTusu, self.sagaDon)
        anaPencere.bind(asagiYonTusu, self.asagiDon)
        anaPencere.bind(solYonTusu, self.solaDon)
        anaPencere.bind(yukariYonTusu, self.yukariDon)
    
    
    
    def run(self):
        while True:
            # yılanı göster
            self.yilanGoster(self.oyun.saha.canvasDizisiSaha, self.oyun.saha.sahaRengi)
            self.oyun.anaPencere.update()    # Pencereyi guncelle
            self.hareketEt()    # yilani hareket ettir
    
    
    
    # yılanı göster
    def yilanGoster(self, canvasDizisiSaha, sahaRengi):
        if self.yilanYasiyorMu == True:
            ### yilani gosterme
            # önce önceki yılanı sil
            self.oncekiYilanSil(canvasDizisiSaha, sahaRengi)
            
            # sonra yılanı göster
            for dizi in self.koordinatlarim:
                canvasDizisiSaha[dizi[0]][dizi[1]].configure(bg = self.renk)
    
    
    
    def oncekiYilanSil(self, canvasDizisiSaha, sahaRengi):
        # yilanin onceki durumunu silme
        # kisaca son parcasini silme
        sonParcaX = self.oncekiKoordinatlarim[len(self.oncekiKoordinatlarim) - 1][0]
        sonParcaY = self.oncekiKoordinatlarim[len(self.oncekiKoordinatlarim) - 1][1]
        canvasDizisiSaha[sonParcaX][sonParcaY].configure(bg = sahaRengi)
    
    
    
    # saga don
    def sagaDon(self, event = None):
        if self.yon == 2:
            self.yon = 1
        if self.yon == 4:
            self.yon = 1
    
    # asagi don
    def asagiDon(self, event = None):
        if self.yon == 1:
            self.yon = 2
        if self.yon == 3:
            self.yon = 2
    
    # sola don
    def solaDon(self, event = None):
        if self.yon == 2:
            self.yon = 3
        if self.yon == 4:
            self.yon = 3
    
    # yukari don
    def yukariDon(self, event = None):
        if self.yon == 1:
            self.yon = 4
        if self.yon == 3:
            self.yon = 4
    
    def hareketEt(self):
        if self.yilanYasiyorMu == True and self.yilanHareketEdiyorMu == True:
            # belirli bir süre bekle
            sleep(self.beklemeSuresi)
            
            
            
            # onceki koordinatlari her hareket oncesinde belirle
            for sayac in range(len(self.koordinatlarim)):
                for sayac2 in range(len(self.koordinatlarim[sayac])):
                    self.oncekiKoordinatlarim[sayac][sayac2] = self.koordinatlarim[sayac][sayac2]
            
            # yilanin basini belirli olan yonde bir adim goturme
            if self.yon == 1:    # eger yon sagsa...
                self.koordinatlarim[0][1] += 1    # koordinat y'yi 1 artir
            if self.yon == 2:    # eger yon asagiysa...
                self.koordinatlarim[0][0] += 1    # koordinat x'i 1 artir
            if self.yon == 3:    # eger yon solsa...
                self.koordinatlarim[0][1] -= 1    # koordinat y'yi 1 azalt
            if self.yon == 4:    # eger yon yukariysa...
                self.koordinatlarim[0][0] -= 1    # koordinat x'i 1 azalt
            
            # yilanin diger parcalarinin kendinden bir sonraki parcanin
            # bir hareket oncesinde bulunan yere konmasi...
            boyut = len(self.koordinatlarim) - 1
            for sayac in range(boyut):
                boyut2 = len(self.koordinatlarim[sayac])
                for sayac2 in range(boyut2):
                    self.koordinatlarim[sayac + 1][sayac2] = self.oncekiKoordinatlarim[sayac][sayac2]
            
            
            
            # duruma bak
            durum = self.durumDegerlendir(self.oyun.saha.sahaBoyutlari, self.oyun.yem.yemKoor,
                                          self.oyun.bilgi.bilgiAl, self.oyun.bilgi.bilgiGoster)
            if durum == 0:    # eger yilan bir duvara veya kendine carpmissa... 
                self.yilaniOldur(self.oyun.bilgi.bilgiAl, self.oyun.bilgi.bilgiGoster)    # yılanı öldür
            elif durum == 1:    # eger carpma yok ama yilan yem yemisse...
                self.beslen()    # yilan beslensin
                
                ## Göster
                # yılanı göster
                self.yilanGoster(self.oyun.saha.canvasDizisiSaha, self.oyun.saha.sahaRengi)
                self.oyun.anaPencere.update()    # Pencereyi guncelle
                
                # yeni yem koyma
                self.oyun.yem.yeminYeriniAyarla(self.oyun.saha.sahaBoyutlari, self.koordinatlarim)
                
                # yemi goster
                self.oyun.yem.yemGoster(self.oyun.saha.canvasDizisiSaha)
    
    
    
    def beslen(self):
        # yilanin onceki pozisyonundaki en son birimini yilanin yeni pozisyonuna ekle.
        # boylece yilan bir birim buyumus olur
        x = self.oncekiKoordinatlarim[len(self.oncekiKoordinatlarim) - 1][0]
        y = self.oncekiKoordinatlarim[len(self.oncekiKoordinatlarim) - 1][1]
        self.koordinatlarim.append([x, y])
        # "koordinatlarim" listesinin buyumesine paralel olarak
        # "oncekiKoordinatlarim" listesini de buyut
        self.oncekiKoordinatlarim.append([1, 1])
    
    
    
    # carpisma varsa 0 dondurur.
    # yem yenmisse 1 dondurur.
    # bunlarin hicbiri olmamissa 2 dondurur.
    def durumDegerlendir(self, sahaBoyutlari, yemKoor, bilgiGonder, bilgiGoster):
        if self.carpismaVarMi(sahaBoyutlari, bilgiGonder, bilgiGoster):
            return 0
        
        elif self.yemYenmisMi(yemKoor, bilgiGonder, bilgiGoster):
            return 1
        else:
            return 2
    
    
    
    def carpismaVarMi(self, sahaBoyutlari, bilgiGonder, bilgiGoster):
        carpmaVarMi = False
        # eger yilan sirasiyla sol duvara, ust duvara, sag duvara veya alt duvara carpmissa...
        if self.koordinatlarim[0][0] == -1 or \
           self.koordinatlarim[0][1] == -1 or \
           self.koordinatlarim[0][0] == sahaBoyutlari[1] or \
           self.koordinatlarim[0][1] == sahaBoyutlari[0]:
            # Çarpma olduğu bilgisini göster
            bilgiGonder("Duvara carptin!")
            bilgiGoster()
            carpmaVarMi = True
        
        # eger yilan herhangi bir sekilde kendine carpmissa...
        for liste in self.koordinatlarim[3:]:
            if liste == self.koordinatlarim[0]:
                # Çarpma olduğu bilgisini göster
                bilgiGonder("Kendine carptin!")
                bilgiGoster()
                carpmaVarMi = True
        
        return carpmaVarMi
    
    
    
    def yemYenmisMi(self, yemKoor, bilgiGonder, bilgiGoster):
        if self.koordinatlarim[0] == yemKoor:
            # Yem yendiği bilgisini göster
            bilgiGonder("Yem yedin!")
            bilgiGoster()
            return True
        else:
            return False
    
    
    def yilaniDuraklatDevamEttir(self):
        if self.yilanHareketEdiyorMu == True:
            self.yilanHareketEdiyorMu = False
        elif self.yilanHareketEdiyorMu == False:
            self.yilanHareketEdiyorMu = True
    
    
    # yılanı öldür
    def yilaniOldur(self, bilgiGonder, bilgiGoster):
        self.yilanYasiyorMu = False
        bilgiGonder("Yilan oldu!")
        bilgiGoster()





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