#-*-coding=utf-8-*-

# içe aktarmalar
from threading import Thread
from math import sqrt
import time

# yılanı kontrol edecek olan yapay zeka
class YapayZeka(Thread):
    def __init__(self, oyun, yilan, yemKoor, sahaBoyutlari, yilanlar):
        Thread.__init__(self)
        self.ilkBildirimYap(oyun, yilan, yemKoor, sahaBoyutlari, yilanlar)
    
    def ilkBildirimYap(self, oyun, yilan, yemKoor, sahaBoyutlari, yilanlar):
        self.oyun = oyun
        self.yilan = yilan    # yapay zekanın kontrol edeceği yılan
        self.gidilebilecekYonler = [1, 2, 4]
        self.yemKoor = yemKoor
        self.sahaBoyutlari = sahaBoyutlari
        self.yilanlar = yilanlar
    
    
    
    def run(self):
        while True:
            """self.yilan.yilaniDuraklatDevamEttir()"""
            
            """time.sleep(self.yilan.beklemeSuresi - 0.02)"""
            
            
            """zamanBas = time.time()"""
            
            
            self.yonuBelirle(self.yemKoor, self.sahaBoyutlari, self.yilanlar)
            
            """zamanSon = time.time()"""
            
            
            if self.gidilebilecekYonler[0] == 1:
                self.yilan.sagaDon()
            if self.gidilebilecekYonler[0] == 2:
                self.yilan.asagiDon()
            if self.gidilebilecekYonler[0] == 3:
                self.yilan.solaDon()
            if self.gidilebilecekYonler[0] == 4:
                self.yilan.yukariDon()
            
            
            """self.yilan.yilaniDuraklatDevamEttir()"""
            
            
            # yılanı göster
            self.yilan.yilanGoster(self.oyun.saha.canvasDizisiSaha, self.oyun.saha.sahaRengi)
            self.oyun.arayuz.anaPencere.update()    # Pencereyi guncelle
            self.yilan.hareketEt()    # yilani hareket ettir
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ########################### DÜŞÜNME SÜRECİ ########################################
    # hareketten önce gidilecek yonu belirle
    def yonuBelirle(self, yemKoor, sahaBoyutlari, yilanlar):
        # en başta gidilmesi mümkün olan yönleri belirle
        # (sahanın dışı olmayan ve herhangi bir yılanın üstüne denk gelmeyen yönler)
        self.mumkunYonlerBelirle(sahaBoyutlari, yilanlar)
        
        """
        # mümkün yön yok ise yılanı öldür
        if len(self.gidilebilecekYonler) == 0:
            self.yilanYasiyorMu = False
            if self.yilan.koordinatlarim[0][1] == sahaBoyutlari[0]:
                self.gidilebilecekYonler = [3]
            elif self.yilan.koordinatlarim[0][1] == 0:
                self.gidilebilecekYonler = [1]
            elif self.yilan.koordinatlarim[0][0] == sahaBoyutlari[1]:
                self.gidilebilecekYonler = [4]
            elif self.yilan.koordinatlarim[0][0] == 0:
                self.gidilebilecekYonler = [2]
            else:
                self.gidilebilecekYonler = [1]
            while True:
                if self.yilan.koordinatlarim[-1] == self.yilan.koordinatlarim[0]:
                    break
                del self.yilan.koordinatlarim[-1]
                del self.oncekiKoordinatlarim[-1]
            
            
            return"""
        
        # tek yön var ise çağırıcı fonksiyona geri dön
        if len(self.gidilebilecekYonler) == 1:
            return
        
        
        
        
        self.hayatinaGoreYonlerBelirle4(sahaBoyutlari, yilanlar)
        """self.hayatinaGoreYonlerBelirle3(sahaBoyutlari, yilanlar)"""
        """self.hayatinaGoreYonlerBelirle2(sahaBoyutlari, yilanlar)"""
        # yılanın devam ederse ölmeyeceği yönleri belirle
        """self.hayatinaGoreYonlerBelirle(sahaBoyutlari, yilanlar)"""
        
        
        
        # robot yılanı yeme en kısa yoldan götürecek yönleri belirle
        self.yemeGoreYonlerBelirle(yemKoor)
    
    
    
    
    
    
    
    
    
    
    
    def hayatinaGoreYonlerBelirle4(self, sahaBoyutlari, yilanlar):
        # tek belirteçli iki öğeli bir liste alır ve
        # bu listenin içindeki koordinatların yılanın üstünde olup olmadığını döndürür
        def koorYilanUstundeMi(koor):
            if koor in self.yilan.koordinatlarim:
                return True
            else:
                return False
        
        # tek belirteçli iki öğeli bir liste alır ve
        # bu listenin içindeki koordinatların sahanın dışında olup olmadığını döndürür
        def koorSahaDisindaMi(koor):
            if koor[0] == -1 or koor[1] == -1 or \
               koor[0] == sahaBoyutlari[1] or koor[1] == sahaBoyutlari[0]:
                return True
            else:
                return False
        
        
        
        def koorYilanParcalariKenarKoseAyarla():
            # yılanın parçalarının kenar ve köşe koordinatlarını bulma
            koorYilanParcaKenarKose = []    # kenar ve köşe koordinatlarını tutan liste
            # yılanın parçalarının kenar ve köşe koordinatlarını
            # listeye sırasıyla yazdır
            for sayac in range(0, len(self.yilan.koordinatlarim)):
                koorYilanParcaKenarKose += [[self.yilan.koordinatlarim[sayac][0] - 1,
                                            self.yilan.koordinatlarim[sayac][1]],
                                           [self.yilan.koordinatlarim[sayac][0] + 1,
                                            self.yilan.koordinatlarim[sayac][1]],
                                           [self.yilan.koordinatlarim[sayac][0],
                                            self.yilan.koordinatlarim[sayac][1] - 1],
                                           [self.yilan.koordinatlarim[sayac][0],
                                            self.yilan.koordinatlarim[sayac][1] + 1],
                                           [self.yilan.koordinatlarim[sayac][0] - 1,
                                            self.yilan.koordinatlarim[sayac][1] - 1],
                                           [self.yilan.koordinatlarim[sayac][0] - 1,
                                            self.yilan.koordinatlarim[sayac][1] + 1],
                                           [self.yilan.koordinatlarim[sayac][0] + 1,
                                            self.yilan.koordinatlarim[sayac][1] - 1],
                                           [self.yilan.koordinatlarim[sayac][0] + 1,
                                            self.yilan.koordinatlarim[sayac][1] + 1]]
            
            
            # yılan üstünde olan ve saha dışında olan "koor" ları çıkar
            yeniKoorYilanParcaKenarKose = []
            for koor in koorYilanParcaKenarKose:
                if (koorYilanUstundeMi(koor) == False) and (koorSahaDisindaMi(koor) == False):
                    yeniKoorYilanParcaKenarKose.append(koor[:])
            koorYilanParcaKenarKose = yeniKoorYilanParcaKenarKose
            
            
            return koorYilanParcaKenarKose
        
        
        def sifirIleBirYanyanaVarMi(koorYilanParcaKenarKose, nolar):
            durum = False
            
            sayac = 0
            for no in nolar:
                if no == 0:
                    sagKoor = [koorYilanParcaKenarKose[sayac][0], koorYilanParcaKenarKose[sayac][1] + 1]
                    asagiKoor = [koorYilanParcaKenarKose[sayac][0] + 1, koorYilanParcaKenarKose[sayac][1]]
                    solKoor = [koorYilanParcaKenarKose[sayac][0], koorYilanParcaKenarKose[sayac][1] - 1]
                    yukariKoor = [koorYilanParcaKenarKose[sayac][0] - 1, koorYilanParcaKenarKose[sayac][1]]
                    
                    if sagKoor in koorYilanParcaKenarKose:
                        sagKoorNo = koorYilanParcaKenarKose.index(sagKoor)
                        if nolar[sagKoorNo] == 1:
                            durum = True
                    if asagiKoor in koorYilanParcaKenarKose:
                        asagiKoorNo = koorYilanParcaKenarKose.index(asagiKoor)
                        if nolar[asagiKoorNo] == 1:
                            durum = True
                    if solKoor in koorYilanParcaKenarKose:
                        solKoorNo = koorYilanParcaKenarKose.index(solKoor)
                        if nolar[solKoorNo] == 1:
                            durum = True
                    if yukariKoor in koorYilanParcaKenarKose:
                        yukariKoorNo = koorYilanParcaKenarKose.index(yukariKoor)
                        if nolar[yukariKoorNo] == 1:
                            durum = True
                    
                sayac += 1
            
            return durum
        
        
        
        
        
        koorYilanParcaKenarKose = koorYilanParcalariKenarKoseAyarla()
        
        # Her "koor" u tekleştir
        koorYilanParcaKenarKose2 = []
        for koor in koorYilanParcaKenarKose:
            if koor not in koorYilanParcaKenarKose2:
                koorYilanParcaKenarKose2.append(koor[:])
        koorYilanParcaKenarKose = koorYilanParcaKenarKose2
        
        
        
        
        
        
        
        
        
        
        
        
        yeniGidilebilecekYonler = []
        for yon in self.gidilebilecekYonler:
            if yon == 1:    # sağ için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sağa gidildiğinde satır değişmez, sütun artar)
                koorKafaIleri = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                if koorKafaIleri in koorYilanParcaKenarKose:
                    koorYilanParcaKenarKose.remove(koorKafaIleri)
                koorKuyruk = [self.yilan.koordinatlarim[-1][0], self.yilan.koordinatlarim[-1][1]]
                yeniKoorYilanParcaKenarKose = [koorKafaIleri] + koorYilanParcaKenarKose + \
                                              [koorKuyruk]
                
                nolar = [0 for i in range(len(yeniKoorYilanParcaKenarKose))]
                nolar[0] = 1
                
                while sifirIleBirYanyanaVarMi(yeniKoorYilanParcaKenarKose, nolar) == True:
                    """for i in range(50):"""
                    """no = nolar.index(1)"""
                    nolar2 = nolar[:]
                    
                    sayacNo = 0
                    for no in nolar2:
                        if no == 1:
                            sagKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0], yeniKoorYilanParcaKenarKose[sayacNo][1] + 1]
                            asagiKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0] + 1, yeniKoorYilanParcaKenarKose[sayacNo][1]]
                            solKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0], yeniKoorYilanParcaKenarKose[sayacNo][1] - 1]
                            yukariKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0] - 1, yeniKoorYilanParcaKenarKose[sayacNo][1]]
                            
                            if sagKoor in yeniKoorYilanParcaKenarKose:
                                sagKoorNo = yeniKoorYilanParcaKenarKose.index(sagKoor)
                                if nolar[sagKoorNo] == 0:
                                    nolar[sagKoorNo] = 1
                            if asagiKoor in yeniKoorYilanParcaKenarKose:
                                asagiKoorNo = yeniKoorYilanParcaKenarKose.index(asagiKoor)
                                if nolar[asagiKoorNo] == 0:
                                    nolar[asagiKoorNo] = 1
                            if solKoor in yeniKoorYilanParcaKenarKose:
                                solKoorNo = yeniKoorYilanParcaKenarKose.index(solKoor)
                                if nolar[solKoorNo] == 0:
                                    nolar[solKoorNo] = 1
                            if yukariKoor in yeniKoorYilanParcaKenarKose:
                                yukariKoorNo = yeniKoorYilanParcaKenarKose.index(yukariKoor)
                                if nolar[yukariKoorNo] == 0:
                                    nolar[yukariKoorNo] = 1
                        sayacNo += 1
                
                if nolar[-1] == 1:
                    yeniGidilebilecekYonler.append(yon)
            
            
            if yon == 2:    # aşağı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (aşağı gidildiğinde satır artar, sütun değişmez)
                koorKafaIleri = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                if koorKafaIleri in koorYilanParcaKenarKose:
                    koorYilanParcaKenarKose.remove(koorKafaIleri)
                koorKuyruk = [self.yilan.koordinatlarim[-1][0], self.yilan.koordinatlarim[-1][1]]
                yeniKoorYilanParcaKenarKose = [koorKafaIleri] + koorYilanParcaKenarKose + \
                                              [koorKuyruk]
                nolar = [0 for i in range(len(yeniKoorYilanParcaKenarKose))]
                nolar[0] = 1
                
                while sifirIleBirYanyanaVarMi(yeniKoorYilanParcaKenarKose, nolar) == True:
                    """for i in range(50):"""
                    """no = nolar.index(1)"""
                    nolar2 = nolar[:]
                    
                    sayacNo = 0
                    for no in nolar2:
                        if no == 1:
                            sagKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0], yeniKoorYilanParcaKenarKose[sayacNo][1] + 1]
                            asagiKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0] + 1, yeniKoorYilanParcaKenarKose[sayacNo][1]]
                            solKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0], yeniKoorYilanParcaKenarKose[sayacNo][1] - 1]
                            yukariKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0] - 1, yeniKoorYilanParcaKenarKose[sayacNo][1]]
                            if sagKoor in yeniKoorYilanParcaKenarKose:
                                sagKoorNo = yeniKoorYilanParcaKenarKose.index(sagKoor)
                                if nolar[sagKoorNo] == 0:
                                    nolar[sagKoorNo] = 1
                            if asagiKoor in yeniKoorYilanParcaKenarKose:
                                asagiKoorNo = yeniKoorYilanParcaKenarKose.index(asagiKoor)
                                if nolar[asagiKoorNo] == 0:
                                    nolar[asagiKoorNo] = 1
                            if solKoor in yeniKoorYilanParcaKenarKose:
                                solKoorNo = yeniKoorYilanParcaKenarKose.index(solKoor)
                                if nolar[solKoorNo] == 0:
                                    nolar[solKoorNo] = 1
                            if yukariKoor in yeniKoorYilanParcaKenarKose:
                                yukariKoorNo = yeniKoorYilanParcaKenarKose.index(yukariKoor)
                                if nolar[yukariKoorNo] == 0:
                                    nolar[yukariKoorNo] = 1
                        sayacNo += 1
                
                if nolar[-1] == 1:
                    yeniGidilebilecekYonler.append(yon)
            
            
            if yon == 3:    # sol için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sola gidildiğinde satır değişmez, sütun azalır)
                koorKafaIleri = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                if koorKafaIleri in koorYilanParcaKenarKose:
                    koorYilanParcaKenarKose.remove(koorKafaIleri)
                koorKuyruk = [self.yilan.koordinatlarim[-1][0], self.yilan.koordinatlarim[-1][1]]
                yeniKoorYilanParcaKenarKose = [koorKafaIleri] + koorYilanParcaKenarKose + \
                                              [koorKuyruk]
                nolar = [0 for i in range(len(yeniKoorYilanParcaKenarKose))]
                nolar[0] = 1
                
                while sifirIleBirYanyanaVarMi(yeniKoorYilanParcaKenarKose, nolar) == True:
                    """for i in range(50):"""
                    """no = nolar.index(1)"""
                    nolar2 = nolar[:]
                    
                    sayacNo = 0
                    for no in nolar2:
                        if no == 1:
                            sagKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0], yeniKoorYilanParcaKenarKose[sayacNo][1] + 1]
                            asagiKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0] + 1, yeniKoorYilanParcaKenarKose[sayacNo][1]]
                            solKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0], yeniKoorYilanParcaKenarKose[sayacNo][1] - 1]
                            yukariKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0] - 1, yeniKoorYilanParcaKenarKose[sayacNo][1]]
                            if sagKoor in yeniKoorYilanParcaKenarKose:
                                sagKoorNo = yeniKoorYilanParcaKenarKose.index(sagKoor)
                                if nolar[sagKoorNo] == 0:
                                    nolar[sagKoorNo] = 1
                            if asagiKoor in yeniKoorYilanParcaKenarKose:
                                asagiKoorNo = yeniKoorYilanParcaKenarKose.index(asagiKoor)
                                if nolar[asagiKoorNo] == 0:
                                    nolar[asagiKoorNo] = 1
                            if solKoor in yeniKoorYilanParcaKenarKose:
                                solKoorNo = yeniKoorYilanParcaKenarKose.index(solKoor)
                                if nolar[solKoorNo] == 0:
                                    nolar[solKoorNo] = 1
                            if yukariKoor in yeniKoorYilanParcaKenarKose:
                                yukariKoorNo = yeniKoorYilanParcaKenarKose.index(yukariKoor)
                                if nolar[yukariKoorNo] == 0:
                                    nolar[yukariKoorNo] = 1
                        sayacNo += 1
                
                if nolar[-1] == 1:
                    yeniGidilebilecekYonler.append(yon)
            
            
            if yon == 4:    # yukarı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (yukarı gidildiğinde satır azalır, sütun değişmez)
                koorKafaIleri = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                if koorKafaIleri in koorYilanParcaKenarKose:
                    koorYilanParcaKenarKose.remove(koorKafaIleri)
                koorKuyruk = [self.yilan.koordinatlarim[-1][0], self.yilan.koordinatlarim[-1][1]]
                yeniKoorYilanParcaKenarKose = [koorKafaIleri] + koorYilanParcaKenarKose + \
                                              [koorKuyruk]
                nolar = [0 for i in range(len(yeniKoorYilanParcaKenarKose))]
                nolar[0] = 1
                
                while sifirIleBirYanyanaVarMi(yeniKoorYilanParcaKenarKose, nolar) == True:
                    """for i in range(50):"""
                    """no = nolar.index(1)"""
                    nolar2 = nolar[:]
                    
                    sayacNo = 0
                    for no in nolar2:
                        if no == 1:
                            sagKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0], yeniKoorYilanParcaKenarKose[sayacNo][1] + 1]
                            asagiKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0] + 1, yeniKoorYilanParcaKenarKose[sayacNo][1]]
                            solKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0], yeniKoorYilanParcaKenarKose[sayacNo][1] - 1]
                            yukariKoor = [yeniKoorYilanParcaKenarKose[sayacNo][0] - 1, yeniKoorYilanParcaKenarKose[sayacNo][1]]
                            if sagKoor in yeniKoorYilanParcaKenarKose:
                                sagKoorNo = yeniKoorYilanParcaKenarKose.index(sagKoor)
                                if nolar[sagKoorNo] == 0:
                                    nolar[sagKoorNo] = 1
                            if asagiKoor in yeniKoorYilanParcaKenarKose:
                                asagiKoorNo = yeniKoorYilanParcaKenarKose.index(asagiKoor)
                                if nolar[asagiKoorNo] == 0:
                                    nolar[asagiKoorNo] = 1
                            if solKoor in yeniKoorYilanParcaKenarKose:
                                solKoorNo = yeniKoorYilanParcaKenarKose.index(solKoor)
                                if nolar[solKoorNo] == 0:
                                    nolar[solKoorNo] = 1
                            if yukariKoor in yeniKoorYilanParcaKenarKose:
                                yukariKoorNo = yeniKoorYilanParcaKenarKose.index(yukariKoor)
                                if nolar[yukariKoorNo] == 0:
                                    nolar[yukariKoorNo] = 1
                        sayacNo += 1
                
                if nolar[-1] == 1:
                    yeniGidilebilecekYonler.append(yon)
        
        
        if len(yeniGidilebilecekYonler) != 0:
            self.gidilebilecekYonler = yeniGidilebilecekYonler
    
    
    
    
    
    
    
    
    
    
    
    # yılanın kuyruğundan bir önceki koordinatın direk gördüğü duvarları belirle,
    # yılanın başından bir sonraki koordinatın direk gördüğü duvarları belirle,
    # bu duvarlardan en az biri eşleşirse o yönden gidilebilir
    # çünkü o yönden gidildiğinde yılanın başı ile kuyruğu birbirine ulaşabilir demektir
    # ancak hiçbiri eşleşmezse o yönden gidilemez
    def hayatinaGoreYonlerBelirle3(self, sahaBoyutlari, yilanlar):
        
        global SAGDUVAR
        global ASAGIDUVAR
        global SOLDUVAR
        global YUKARIDUVAR
        SAGDUVAR = 1
        ASAGIDUVAR = 2
        SOLDUVAR = 3
        YUKARIDUVAR = 4
        
        # "koor" un; "sahaBoyutlari" içindeki boyutlara göre, "yilanKoordinatlari" içindeki
        # koordinatlara denk gelmeden, direk gördüğü duvarları bir listeye ata ve döndür
        def gorulenDuvarlariBelirleDondur(koor, sahaBoyutlari, yilanKoorlari):
            # koordan sağ duvara giden koordinatların listesi
            sagKoorlar = [[koor[0], i] for i in range(koor[1] + 1, sahaBoyutlari[0])]
            # koordan aşağı duvara giden koordinatların listesi
            asagiKoorlar = [[i, koor[1]] for i in range(koor[0] + 1, sahaBoyutlari[1])]
            # koordan sol duvara giden koordinatların listesi
            solKoorlar = [[koor[0], i] for i in range(koor[1] - 1, -1, -1)]
            # koordan yukarı duvara giden koordinatların listesi
            yukariKoorlar = [[i, koor[1]] for i in range(koor[0] - 1, -1, -1)]
            
            gorulenDuvarlar = []
            kosul = True
            for koor in sagKoorlar:
                if koor in yilanKoorlari:
                    kosul = False
            if kosul == True or len(sagKoorlar) == 0:
                gorulenDuvarlar.append(SAGDUVAR)
            
            kosul = True
            for koor in asagiKoorlar:
                if koor in yilanKoorlari:
                    kosul = False
            if kosul == True or len(asagiKoorlar) == 0:
                gorulenDuvarlar.append(ASAGIDUVAR)
            
            kosul = True
            for koor in solKoorlar:
                if koor in yilanKoorlari:
                    kosul = False
            if kosul == True or len(solKoorlar) == 0:
                gorulenDuvarlar.append(SOLDUVAR)
            
            kosul = True
            for koor in yukariKoorlar:
                if koor in yilanKoorlari:
                    kosul = False
            if kosul == True or len(yukariKoorlar) == 0:
                gorulenDuvarlar.append(YUKARIDUVAR)
            
            return gorulenDuvarlar    # döndür
        
        
        # "self.gidilebilecekYonler" listesindeki her yön için durumları incele
        yeniGidilebilecekYonler = []
        for yon in self.gidilebilecekYonler:
            if yon == 1:    # sağ için
                # bu yönde gidildiğinde kafanın ulaşacağı koordinat
                # (sağa gidildiğinde satır değişmez, sütun artar)
                kafaIleriKoor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                # kuyruğun bir sonraki koordinatı
                # (kuyruğun önündeki parçanın koordinatı)
                kuyrukIleriKoor = [self.yilan.koordinatlarim[-1][0], self.yilan.koordinatlarim[-1][1]]
                # kafanın önündeki koordinattan görülen duvarları listeye ata
                gorulenDuvarlarKafa = gorulenDuvarlariBelirleDondur(kafaIleriKoor, sahaBoyutlari,
                                                                    self.yilan.koordinatlarim)
                # kuyruğun önündeki koordinattan görülen duvarları listeye ata
                gorulenDuvarlarKuyruk = gorulenDuvarlariBelirleDondur(kuyrukIleriKoor, sahaBoyutlari,
                                                                      self.yilan.koordinatlarim)
                kosul = False
                for duvar in gorulenDuvarlarKafa:
                    if duvar in gorulenDuvarlarKuyruk:
                        kosul = True
                if kosul == True:
                    yeniGidilebilecekYonler.append(yon)
            
            if yon == 2:    # aşağı için
                # bu yönde gidildiğinde kafanın ulaşacağı koordinat
                # (aşağı gidildiğinde satır artar, sütun değişmez)
                kafaIleriKoor = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                # kuyruğun bir sonraki koordinatı
                # (kuyruğun önündeki parçanın koordinatı)
                kuyrukIleriKoor = [self.yilan.koordinatlarim[-1][0], self.yilan.koordinatlarim[-1][1]]
                # kafanın önündeki koordinattan görülen duvarları listeye ata
                gorulenDuvarlarKafa = gorulenDuvarlariBelirleDondur(kafaIleriKoor, sahaBoyutlari,
                                                                    self.yilan.koordinatlarim)
                # kuyruğun önündeki koordinattan görülen duvarları listeye ata
                gorulenDuvarlarKuyruk = gorulenDuvarlariBelirleDondur(kuyrukIleriKoor, sahaBoyutlari,
                                                                      self.yilan.koordinatlarim)
                kosul = False
                for duvar in gorulenDuvarlarKafa:
                    if duvar in gorulenDuvarlarKuyruk:
                        kosul = True
                if kosul == True:
                    yeniGidilebilecekYonler.append(yon)
            
            if yon == 3:    # sol için
                # bu yönde gidildiğinde kafanın ulaşacağı koordinat
                # (sola gidildiğinde satır değişmez, sütun azalır)
                kafaIleriKoor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                # kuyruğun bir sonraki koordinatı
                # (kuyruğun önündeki parçanın koordinatı)
                kuyrukIleriKoor = [self.yilan.koordinatlarim[-1][0], self.yilan.koordinatlarim[-1][1]]
                # kafanın önündeki koordinattan görülen duvarları listeye ata
                gorulenDuvarlarKafa = gorulenDuvarlariBelirleDondur(kafaIleriKoor, sahaBoyutlari,
                                                                    self.yilan.koordinatlarim)
                # kuyruğun önündeki koordinattan görülen duvarları listeye ata
                gorulenDuvarlarKuyruk = gorulenDuvarlariBelirleDondur(kuyrukIleriKoor, sahaBoyutlari,
                                                                      self.yilan.koordinatlarim)
                kosul = False
                for duvar in gorulenDuvarlarKafa:
                    if duvar in gorulenDuvarlarKuyruk:
                        kosul = True
                if kosul == True:
                    yeniGidilebilecekYonler.append(yon)
            
            if yon == 4:    # yukarı için
                # bu yönde gidildiğinde kafanın ulaşacağı koordinat
                # (yukarı gidildiğinde satır azalır, sütun değişmez)
                kafaIleriKoor = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                # kuyruğun bir sonraki koordinatı
                # (kuyruğun önündeki parçanın koordinatı)
                kuyrukIleriKoor = [self.yilan.koordinatlarim[-1][0], self.yilan.koordinatlarim[-1][1]]
                # kafanın önündeki koordinattan görülen duvarları listeye ata
                gorulenDuvarlarKafa = gorulenDuvarlariBelirleDondur(kafaIleriKoor, sahaBoyutlari,
                                                                    self.yilan.koordinatlarim)
                # kuyruğun önündeki koordinattan görülen duvarları listeye ata
                gorulenDuvarlarKuyruk = gorulenDuvarlariBelirleDondur(kuyrukIleriKoor, sahaBoyutlari,
                                                                      self.yilan.koordinatlarim)
                kosul = False
                for duvar in gorulenDuvarlarKafa:
                    if duvar in gorulenDuvarlarKuyruk:
                        kosul = True
                if kosul == True:
                    yeniGidilebilecekYonler.append(yon)
        
        if len(yeniGidilebilecekYonler) != 0:
            self.gidilebilecekYonler = yeniGidilebilecekYonler
    
    
    
    # sahayı bölgelere ayır ve
    # yılanın yöne göre bir adım sonra olacağı bölgeyle yılanın kuyruğunun aynı bölgede olup olmadığını
    # kontrol et
    # aynı bölgedeyse o zaman bu yöne gidilebilir
    # değilse bu yönden gidilemez
    def hayatinaGoreYonlerBelirle2(self, sahaBoyutlari, yilanlar):
        # sahanın boyutlarını ve içindeki yılanın koordinatlarını alır ve
        # duvarlarla birlikte sahayı listeleştirir ve bu listeyi döndürür
        # (saha boyutlarının genişlik ve yükseklik olarak iki fazlası boyut olur)
        # duvar ve yılan --> -1
        # diğerleri(ilk atama) --> 0
        # diğerleri(sonraki atamalar) --> 1, 2, 3...
        def sahayiListelestir(sahaBoyutlari, koordinatlar):
            # sahanın listesini bildir
            sahaListesi = []
            # bu listeye sahanın yüksekliğinin iki fazlası kadar liste ekle
            for satirSayaci in range(sahaBoyutlari[1] + 2):
                sahaListesi.append([])
            # eklenen listelerin içini sahanın genişliğinin iki fazlası kadar 0(sıfır) ile doldur
            for liste in sahaListesi:
                for sutunSayaci in range(sahaBoyutlari[0] + 2):
                    liste.append(0)
            ## listedeki ilk satırı, son satırı,ilk sütunu ve son sütunu -1 yap(duvarlar)
            # ilk satır
            for sutunSayaci in range(len(sahaListesi[0])):
                sahaListesi[0][sutunSayaci] = -1
            # son satır
            for sutunSayaci in range(len(sahaListesi[-1])):
                sahaListesi[-1][sutunSayaci] = -1
            # ilk sutun
            for satirSayaci in range(len(sahaListesi)):
                sahaListesi[satirSayaci][0] = -1
            # son sütun
            for satirSayaci in range(len(sahaListesi)):
                sahaListesi[satirSayaci][-1] = -1
            ## sahadaki yılanın koordinatlarını -1 yap
            ## (listede duvarlar da olduğu için yılanın koordinatlarına birer ekleme yapmak gerekir)
            for koor in self.yilan.koordinatlarim:
                sahaListesi[koor[0] + 1][koor[1] + 1] = -1
            return sahaListesi
        
        
        # iki belirteçli bir liste alır ve bu listedeki listeler içinde 0(sıfır)
        # olup olmadığını döndürür
        def listedeSifirVarMi(listeIkili):
            for liste in listeIkili:
                for sayi in liste:
                    if sayi == 0:
                        return True
            
            return False
        
        
        # iki belirteçli bir liste ve bir sayı alır ve
        # bu liste içindeki listelerdeki ilk sıfıra bu sayıyı atar
        # sonunda değişen bu listeyi döndürür
        def listedekiIlkSifiraSayiAta(listeIkili, sayi):
            kosul = True
            for liste in listeIkili:
                if kosul == True:
                    for sayac in range(len(liste)):
                        if liste[sayac] == 0:
                            liste[sayac] = sayi
                            kosul = False
                            break
                else:
                    break
            
            return listeIkili
        
        
        # sahayı listeleştirip bu listeyi "sahaListesi" ne ata
        sahaListesi = sahayiListelestir(sahaBoyutlari, self.yilan.koordinatlarim)
        
        # "sahaListesi" içindeki listelerdeki sayıların sırasıyla eşitleneceği sayıları tutan
        # sayacın tanımı
        numaraSayaci = 1
        # "sahaListesi" nin içindeki listelerde 0(sıfır) var olduğu sürece...
        while listedeSifirVarMi(sahaListesi) == True:
            # "numaraSayaci" ni "sahaListesi" içindeki listelerdeki ilk sıfıra ata
            # fonksiyondan döndürülen liste adresini "sahaListesi" ne ata
            sahaListesi = listedekiIlkSifiraSayiAta(sahaListesi, numaraSayaci)
    
    
    
    # yılanın ilk bakışta gidebileceği yönleri belirle
    # (yılan üstüne gelmeyen ve sahanın içinde olan karelere götüren yönler..)
    def mumkunYonlerBelirle(self, sahaBoyutlari, yilanlar):
        # yılanın şu anki yönüne göre mümkün olan yönleri belirle
        # (sadece yöne bakılarak belirlenir)
        if self.yilan.yon == 1:    # sağ için
            self.gidilebilecekYonler = [1, 2, 4]
        if self.yilan.yon == 2:    # aşağı için
            self.gidilebilecekYonler = [1, 2, 3]
        if self.yilan.yon == 3:    # sol için
            self.gidilebilecekYonler = [2, 3, 4]
        if self.yilan.yon == 4:    # yukarı için
            self.gidilebilecekYonler = [1, 3, 4]
        
        # gidildiğinde sahanın dışına çıkaran yönleri listeden çıkar
        yeniListe = []    # yeni yönlerin geçici olarak tutulacağı liste
        for yon in self.gidilebilecekYonler:
            if yon == 1:    # sağ için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sağa gidildiğinde satır değişmez, sütun artar)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                # eğer koordinatlar sahanın dışında değilse...
                if koor[0] != -1 and koor[0] != sahaBoyutlari[0] and \
                   koor[1] != -1 and koor[1] != sahaBoyutlari[1]:
                    yeniListe.append(yon)    # bu yönü "yeniListe" ye ekle
            
            if yon == 2:    # aşağı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (aşağı gidildiğinde satır artar, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                # eğer koordinatlar sahanın dışında değilse...
                if koor[0] != -1 and koor[0] != sahaBoyutlari[0] and \
                   koor[1] != -1 and koor[1] != sahaBoyutlari[1]:
                    yeniListe.append(yon)    # bu yönü "yeniListe" ye ekle
            
            if yon == 3:    # sol için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sola gidildiğinde satır değişmez, sütun azalır)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                # eğer koordinatlar sahanın dışında değilse...
                if koor[0] != -1 and koor[0] != sahaBoyutlari[0] and \
                   koor[1] != -1 and koor[1] != sahaBoyutlari[1]:
                    yeniListe.append(yon)    # bu yönü "yeniListe" ye ekle
            
            if yon == 4:    # yukarı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (yukarı gidildiğinde satır azalır, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                # eğer koordinatlar sahanın dışında değilse...
                if koor[0] != -1 and koor[0] != sahaBoyutlari[0] and \
                   koor[1] != -1 and koor[1] != sahaBoyutlari[1]:
                    yeniListe.append(yon)    # bu yönü "yeniListe" ye ekle
        
        self.gidilebilecekYonler = yeniListe
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # gidildiğinde herhangi bir yılanın üstüne gelinen yönleri çıkar
        # (kendisi de dahil)
        yeniListe = []    # yeni yönlerin geçici olarak tutulacağı liste
        for yon in self.gidilebilecekYonler:
            if yon == 1:    # sağ için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sağa gidildiğinde satır değişmez, sütun artar)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                ### koordinatların herhangi bir yılanın üstünde olup olmadığını denetleme..
                ## koordinatlar yılan üstünde mi değil mi onu tutan değişken
                ## (eğer bütün testlerden sonra yine "False" ise
                ##  koordinatlar yılan üstünde değil demektir)
                koorYilanUstundeMi = False
                # yılanın kendisi için kontrol..
                if koor in self.yilan.koordinatlarim:
                    koorYilanUstundeMi = True
                
                
                
                """
                # diğer yılanlar için kontrol
                for yilan in yilanlar:
                    if koor in yilan.koordinatlarim:
                        koorYilanUstundeMi = True
                """
                
                
                
                # eğer kontrollerden sonra "koorYilanUstundeMi" "False" ise...
                # (bu, koordinatların yılan üstünde olmadığı anlamına gelir)
                if koorYilanUstundeMi == False:
                    yeniListe.append(yon)    # bu yönü "yeniListe" ye ekle
                
            if yon == 2:    # aşağı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (aşağı gidildiğinde satır artar, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                ### koordinatların herhangi bir yılanın üstünde olup olmadığını denetleme...
                ## koordinatlar yılan üstünde mi değil mi onu tutan değişken
                ## (eğer bütün testlerden sonra yine "False" ise
                ##  koordinatlar yılan üstünde değil demektir)
                koorYilanUstundeMi = False
                # yılanın kendisi için kontrol..
                if koor in self.yilan.koordinatlarim:
                    koorYilanUstundeMi = True
                
                
                
                """
                # diğer yılanlar için kontrol
                for yilan in yilanlar:
                    if koor in yilan.koordinatlarim:
                        koorYilanUstundeMi = True
                """
                
                
                
                # eğer kontrollerden sonra "koorYilanUstundeMi" "False" ise...
                # (bu, koordinatların yılan üstünde olmadığı anlamına gelir)
                if koorYilanUstundeMi == False:
                    yeniListe.append(yon)    # bu yönü "yeniListe" ye ekle
            
            if yon == 3:    # sol için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sola gidildiğinde satır değişmez, sütun azalır)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                ### koordinatların herhangi bir yılanın üstünde olup olmadığını denetleme...
                ## koordinatlar yılan üstünde mi değil mi onu tutan değişken
                ## (eğer bütün testlerden sonra yine "False" ise
                ##  koordinatlar yılan üstünde değil demektir)
                koorYilanUstundeMi = False
                # yılanın kendisi için kontrol..
                if koor in self.yilan.koordinatlarim:
                    koorYilanUstundeMi = True
                
                
                
                """
                # diğer yılanlar için kontrol
                for yilan in yilanlar:
                    if koor in yilan.koordinatlarim:
                        koorYilanUstundeMi = True
                """
                
                
                
                # eğer kontrollerden sonra "koorYilanUstundeMi" "False" ise...
                # (bu, koordinatların yılan üstünde olmadığı anlamına gelir)
                if koorYilanUstundeMi == False:
                    yeniListe.append(yon)    # bu yönü "yeniListe" ye ekle
            
            if yon == 4:    # yukarı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (yukarı gidildiğinde satır azalır, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                ### koordinatların herhangi bir yılanın üstünde olup olmadığını denetleme...
                ## koordinatlar yılan üstünde mi değil mi onu tutan değişken
                ## (eğer bütün testlerden sonra yine "False" ise
                ##  koordinatlar yılan üstünde değil demektir)
                koorYilanUstundeMi = False
                # yılanın kendisi için kontrol..
                if koor in self.yilan.koordinatlarim:
                    koorYilanUstundeMi = True
                
                
                
                """
                # diğer yılanlar için kontrol
                for yilan in yilanlar:
                    if koor in yilan.koordinatlarim:
                        koorYilanUstundeMi = True
                """
                
                
                
                # eğer kontrollerden sonra "koorYilanUstundeMi" "False" ise...
                # (bu, koordinatların yılan üstünde olmadığı anlamına gelir)
                if koorYilanUstundeMi == False:
                    yeniListe.append(yon)    # bu yönü "yeniListe" ye ekle
        
        self.gidilebilecekYonler = yeniListe
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # robot yılanı yeme en kısa yoldan götürecek yönleri belirle
    def yemeGoreYonlerBelirle(self, yemKoor):
        # bir koordinat dizisi alan ve bu koordinatların yeme olan uzaklığını hesaplayan fonksiyon
        def uzaklikHesapla(koor):
            uzaklik1 = koor[0] - yemKoor[0]
            uzaklik2 = koor[1] - yemKoor[1]
            return sqrt(uzaklik1 ** 2 + uzaklik2 ** 2)
        
        # yem için en kısa yola götürecek olan yönü hesapla
        enKisaYon = self.gidilebilecekYonler[0]
        enKisaUzaklik = 1000000
        for yon in self.gidilebilecekYonler:
            if yon == 1:    # sağ için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sağa gidildiğinde satır değişmez, sütun artar)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                uzaklik = uzaklikHesapla(koor)
                if uzaklik < enKisaUzaklik:
                    enKisaUzaklik = uzaklik
                    enKisaYon = yon
            
            if yon == 2:    # aşağı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (aşağı gidildiğinde satır artar, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                uzaklik = uzaklikHesapla(koor)
                if uzaklik < enKisaUzaklik:
                    enKisaUzaklik = uzaklik
                    enKisaYon = yon
            
            if yon == 3:    # sol için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sola gidildiğinde satır değişmez, sütun azalır)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                uzaklik = uzaklikHesapla(koor)
                if uzaklik < enKisaUzaklik:
                    enKisaUzaklik = uzaklik
                    enKisaYon = yon
            
            if yon == 4:    # yukarı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (yukarı gidildiğinde satır azalır, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                uzaklik = uzaklikHesapla(koor)
                if uzaklik < enKisaUzaklik:
                    enKisaUzaklik = uzaklik
                    enKisaYon = yon
        
        self.gidilebilecekYonler = [enKisaYon]
    
    
    
    def yemYenmisMi(self, yemKoor):
        if self.yilan.koordinatlarim[0] == yemKoor:
            # Yem yendiği bilgisini göster
            #self.bilgi.bilgiAl("Yem yedin!")
            #self.bilgi.bilgiGoster()
            return True
        else:
            return False
        
    
    
    
    
    
    # yılanın devam ederse ölmeyeceği yönleri belirle
    def hayatinaGoreYonlerBelirle(self, sahaBoyutlari, yilanlar):
        ### robot yılan için hayatını kesin kaybedeceği bir hareket ancak çıkmaz bir yola girmesiyle olur.
        ### çıkmaz yoldan kasıt, iki yanı kapalı ve sonu da kapalı olan yoldur.
        ### robot yılan için hayatına göre yön belirlemesinin tek amacı böyle bir yola girmemektir.
        
        
        
        # tek belirteçli iki öğeli bir liste alır ve
        # bu listenin içindeki koordinatların yılanın üstünde olup olmadığını döndürür
        def koorYilanUstundeMi(koor):
            if koor in self.yilan.koordinatlarim:
                return True
            else:
                return False
        
        # tek belirteçli iki öğeli bir liste alır ve
        # bu listenin içindeki koordinatların sahanın dışında olup olmadığını döndürür
        def koorSahaDisindaMi(koor):
            if koor[0] == -1 or koor[1] == -1 or \
               koor[0] == sahaBoyutlari[0] or koor[1] == sahaBoyutlari[1]:
                return True
            else:
                return False
        
        def koorYilanParcalarininKenarKosesiMi(koor):
            # yılanın parçalarının kenar ve köşe koordinatlarını bulma
            koorYilanParcaKenarKose = []    # kenar ve köşe koordinatlarını tutan liste
            # yılanın parçalarının kenar ve köşe koordinatlarını
            # listeye sırasıyla yazdır
            for sayac in range(5, len(self.yilan.koordinatlarim) - 1):
                koorYilanParcaKenarKose += [[self.yilan.koordinatlarim[sayac][0] - 1,
                                            self.yilan.koordinatlarim[sayac][1]],
                                           [self.yilan.koordinatlarim[sayac][0] + 1,
                                            self.yilan.koordinatlarim[sayac][1]],
                                           [self.yilan.koordinatlarim[sayac][0],
                                            self.yilan.koordinatlarim[sayac][1] - 1],
                                           [self.yilan.koordinatlarim[sayac][0],
                                            self.yilan.koordinatlarim[sayac][1] + 1],
                                           [self.yilan.koordinatlarim[sayac][0] - 1,
                                            self.yilan.koordinatlarim[sayac][1] - 1],
                                           [self.yilan.koordinatlarim[sayac][0] - 1,
                                            self.yilan.koordinatlarim[sayac][1] + 1],
                                           [self.yilan.koordinatlarim[sayac][0] + 1,
                                            self.yilan.koordinatlarim[sayac][1] - 1],
                                           [self.yilan.koordinatlarim[sayac][0] + 1,
                                            self.yilan.koordinatlarim[sayac][1] + 1]]
            
            if koor in koorYilanParcaKenarKose:
                return True
            else:
                return False
        
        
        
        def koorDuvarinYaniMi(koor, sahaBoyutlari):
            if koor[0] == 0 or koor[0] == sahaBoyutlari[0] or \
               koor[1] == 0 or koor[1] == sahaBoyutlari[1]:
                return True
            else:
                return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ## yılanın kafasını dar bir yere sokmayacağı yönleri seçme
        ## (bu yönler gidildiği zaman kafasını, herhangi bir şekilde iki tarafı kapalı bir yola
        ##  sokmayacağı yönlerdir)
        
        # robot yılanın kafasının sol ve sağ tarafının kapalı olup olmadığını kontrol edip
        # eğer kapalı değilse bu yönü ekleme
        # solu ve sağı kapalı olmayan bir yere götüren yönlerin kaydedileceği liste
        yonlerYeni = self.gidilebilecekYonler[:]
        for yon in self.gidilebilecekYonler:
            if yon == 1:    # sağ için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sağa gidildiğinde satır değişmez, sütun artar)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                # "koor" içindeki koordinatların yöne göre sol ve sağındaki koordinatları hesaplama...
                # satır azalır, sütun değişmez
                solKoor = [koor[0] - 1, koor[1]]
                # satır artar, sütun değişmez
                sagKoor = [koor[0] + 1, koor[1]]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(solKoor) == True or koorSahaDisindaMi(solKoor) == True) and \
                   (koorYilanUstundeMi(sagKoor) == True or koorSahaDisindaMi(sagKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
            
            
            
            if yon == 2:    # aşağı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (aşağı gidildiğinde satır artar, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                # "koor" içindeki koordinatların yöne göre sol ve sağındaki koordinatları hesaplama...
                # satır değişmez, sütun artar
                solKoor = [koor[0], koor[1] + 1]
                # satır değişmez, sütun azalır
                sagKoor = [koor[0], koor[1] - 1]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(solKoor) == True or koorSahaDisindaMi(solKoor) == True) and \
                   (koorYilanUstundeMi(sagKoor) == True or koorSahaDisindaMi(sagKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
            
                   
            
            if yon == 3:    # sol için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sola gidildiğinde satır değişmez, sütun azalır)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                # "koor" içindeki koordinatların yöne göre sol ve sağındaki koordinatları hesaplama...
                # satır artar, sütun değişmez
                solKoor = [koor[0] + 1, koor[1]]
                # satır azalır, sütun değişmez
                sagKoor = [koor[0] - 1, koor[1]]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(solKoor) == True or koorSahaDisindaMi(solKoor) == True) and \
                   (koorYilanUstundeMi(sagKoor) == True or koorSahaDisindaMi(sagKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
            
            
            
            if yon == 4:    # yukarı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (yukarı gidildiğinde satır azalır, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                # "koor" içindeki koordinatların yöne göre sol ve sağındaki koordinatları hesaplama...
                # satır değişmez, sütun azalır
                solKoor = [koor[0], koor[1] - 1]
                # satır değişmez, sütun artar
                sagKoor = [koor[0], koor[1] + 1]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(solKoor) == True or koorSahaDisindaMi(solKoor) == True) and \
                   (koorYilanUstundeMi(sagKoor) == True or koorSahaDisindaMi(sagKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
        
        
        
        
        
        
        
        
        
        
        self.gidilebilecekYonler = yonlerYeni
        
        
        
        
        
        
        
        
        yonlerYeni = self.gidilebilecekYonler[:]
        # robot yılanın kafasının sol ve ön tarafının kapalı olup olmadığını kontrol edip
        # eğer kapalı değilse bu yönü ekleme
        for yon in self.gidilebilecekYonler:
            if yon == 1:    # sağ için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sağa gidildiğinde satır değişmez, sütun artar)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                # "koor" içindeki koordinatların yöne göre sol ve önündeki koordinatları hesaplama...
                # satır azalır, sütun değişmez
                solKoor = [koor[0] - 1, koor[1]]
                # satır değişmez, sütun artar
                onKoor = [koor[0], koor[1] + 1]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(solKoor) == True or koorSahaDisindaMi(solKoor) == True) and \
                   (koorYilanUstundeMi(onKoor) == True or koorSahaDisindaMi(onKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
            
            if yon == 2:    # aşağı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (aşağı gidildiğinde satır artar, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                # "koor" içindeki koordinatların yöne göre sol ve önündeki koordinatları hesaplama...
                # satır değişmez, sütun artar
                solKoor = [koor[0], koor[1] + 1]
                # satır artar, sütun değişmez
                onKoor = [koor[0] + 1, koor[1]]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(solKoor) == True or koorSahaDisindaMi(solKoor) == True) and \
                   (koorYilanUstundeMi(onKoor) == True or koorSahaDisindaMi(onKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
            
            if yon == 3:    # sol için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sola gidildiğinde satır değişmez, sütun azalır)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                # "koor" içindeki koordinatların yöne göre sol ve önündeki koordinatları hesaplama...
                # satır artar, sütun değişmez
                solKoor = [koor[0] + 1, koor[1]]
                # satır değişmez, sütun azalır
                onKoor = [koor[0], koor[1] - 1]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(solKoor) == True or koorSahaDisindaMi(solKoor) == True) and \
                   (koorYilanUstundeMi(onKoor) == True or koorSahaDisindaMi(onKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
            
            if yon == 4:    # yukarı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (yukarı gidildiğinde satır azalır, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                # "koor" içindeki koordinatların yöne göre sol ve önündeki koordinatları hesaplama...
                # satır değişmez, sütun azalır
                solKoor = [koor[0], koor[1] - 1]
                # satır azalır, sütun değişmez
                onKoor = [koor[0] - 1, koor[1]]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(solKoor) == True or koorSahaDisindaMi(solKoor) == True) and \
                   (koorYilanUstundeMi(onKoor) == True or koorSahaDisindaMi(onKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
        
        
        
        
        
        
        
        self.gidilebilecekYonler = yonlerYeni
        
        
        
        
        
        
        yonlerYeni = self.gidilebilecekYonler[:]
        # robot yılanın kafasının sağ ve ön tarafının kapalı olup olmadığını kontrol edip
        # eğer kapalı değilse bu yönü ekleme
        for yon in self.gidilebilecekYonler:
            if yon == 1:    # sağ için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sağa gidildiğinde satır değişmez, sütun artar)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                # "koor" içindeki koordinatların yöne göre sağ ve önündeki koordinatları hesaplama...
                # satır artar, sütun değişmez
                sagKoor = [koor[0] + 1, koor[1]]
                # satır değişmez, sütun artar
                onKoor = [koor[0], koor[1] + 1]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(sagKoor) == True or koorSahaDisindaMi(sagKoor) == True) and \
                   (koorYilanUstundeMi(onKoor) == True or koorSahaDisindaMi(onKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
            
            if yon == 2:    # aşağı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (aşağı gidildiğinde satır artar, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                # "koor" içindeki koordinatların yöne göre sağ ve önündeki koordinatları hesaplama...
                # satır değişmez, sütun azalır
                sagKoor = [koor[0], koor[1] - 1]
                # satır artar, sütun değişmez
                onKoor = [koor[0] + 1, koor[1]]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(sagKoor) == True or koorSahaDisindaMi(sagKoor) == True) and \
                   (koorYilanUstundeMi(onKoor) == True or koorSahaDisindaMi(onKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
            
            if yon == 3:    # sol için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sola gidildiğinde satır değişmez, sütun azalır)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                # "koor" içindeki koordinatların yöne göre sağ ve önündeki koordinatları hesaplama...
                # satır azalır, sütun değişmez
                sagKoor = [koor[0] - 1, koor[1]]
                # satır değişmez, sütun azalır
                onKoor = [koor[0], koor[1] - 1]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(sagKoor) == True or koorSahaDisindaMi(sagKoor) == True) and \
                   (koorYilanUstundeMi(onKoor) == True or koorSahaDisindaMi(onKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
            
            if yon == 4:    # yukarı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (yukarı gidildiğinde satır azalır, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                # "koor" içindeki koordinatların yöne göre sağ ve önündeki koordinatları hesaplama...
                # satır değişmez, sütun artar
                sagKoor = [koor[0], koor[1] + 1]
                # satır azalır, sütun değişmez
                onKoor = [koor[0] - 1, koor[1]]
                # eğer bu koordinatların ikisi birden sahanın dışına çıkıyor ya da
                # yılanın üstüne denk geliyorsa...
                if (koorYilanUstundeMi(sagKoor) == True or koorSahaDisindaMi(sagKoor) == True) and \
                   (koorYilanUstundeMi(onKoor) == True or koorSahaDisindaMi(onKoor) == True):
                    if len(yonlerYeni) > 1:
                        yonlerYeni.remove(yon)    # yeni listeden bu yönü çıkar
        
        
        
        
        
        
        
        
        
        
        
        self.gidilebilecekYonler = yonlerYeni
        
        
        
        
        
        
        
        
        
        # eğer yılanın boyu 8 birimden büyükse...
        if len(self.yilan.koordinatlarim) > 8:
            # "yon" un götürdüğü koordinatın belirli yılan parçalarının köşe veya kenar koordinatları
            # olup olmadığını kontrol et
            yeniGidilebilecekYonler = []
            for yon in self.gidilebilecekYonler:
                if yon == 1:    # sağ için
                    # bu yönde gidildiğinde ulaşılacak koordinat
                    # (sağa gidildiğinde satır değişmez, sütun artar)
                    koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                    if koorYilanParcalarininKenarKosesiMi(koor) == False:
                        yeniGidilebilecekYonler.append(yon)
                if yon == 2:    # aşağı için
                    # bu yönde gidildiğinde ulaşılacak koordinat
                    # (aşağı gidildiğinde satır artar, sütun değişmez)
                    koor = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                    if koorYilanParcalarininKenarKosesiMi(koor) == False:
                        yeniGidilebilecekYonler.append(yon)
                if yon == 3:    # sol için
                    # bu yönde gidildiğinde ulaşılacak koordinat
                    # (sola gidildiğinde satır değişmez, sütun azalır)
                    koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                    if koorYilanParcalarininKenarKosesiMi(koor) == False:
                        yeniGidilebilecekYonler.append(yon)
                if yon == 4:    # yukarı için
                    # bu yönde gidildiğinde ulaşılacak koordinat
                    # (yukarı gidildiğinde satır azalır, sütun değişmez)
                    koor = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                    if koorYilanParcalarininKenarKosesiMi(koor) == False:
                        yeniGidilebilecekYonler.append(yon)
            
            if len(yeniGidilebilecekYonler) != 0:
                self.gidilebilecekYonler = yeniGidilebilecekYonler
        
        
        
        
        # "yon" un götürdüğü koordinatın duvarın yan koordinatları
        # olup olmadığını kontrol et
        yeniGidilebilecekYonler = []
        for yon in self.gidilebilecekYonler:
            if yon == 1:    # sağ için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sağa gidildiğinde satır değişmez, sütun artar)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                if koorDuvarinYaniMi(koor, sahaBoyutlari) == False and \
                   koorDuvarinYaniMi(self.oyun.yem.yemKoor, sahaBoyutlari) == False:
                    yeniGidilebilecekYonler.append(yon)
            if yon == 2:    # aşağı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (aşağı gidildiğinde satır artar, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                if koorDuvarinYaniMi(koor, sahaBoyutlari) == False and \
                   koorDuvarinYaniMi(self.oyun.yem.yemKoor, sahaBoyutlari) == False:
                    yeniGidilebilecekYonler.append(yon)
            if yon == 3:    # sol için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (sola gidildiğinde satır değişmez, sütun azalır)
                koor = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                if koorDuvarinYaniMi(koor, sahaBoyutlari) == False and \
                   koorDuvarinYaniMi(self.oyun.yem.yemKoor, sahaBoyutlari) == False:
                    yeniGidilebilecekYonler.append(yon)
            if yon == 4:    # yukarı için
                # bu yönde gidildiğinde ulaşılacak koordinat
                # (yukarı gidildiğinde satır azalır, sütun değişmez)
                koor = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                if koorDuvarinYaniMi(koor, sahaBoyutlari) == False and \
                   koorDuvarinYaniMi(self.oyun.yem.yemKoor, sahaBoyutlari) == False:
                    yeniGidilebilecekYonler.append(yon)
            
        if len(yeniGidilebilecekYonler) != 0:
            self.gidilebilecekYonler = yeniGidilebilecekYonler
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        # Yılanın kafasının sol çaprazındaki koordinatları döndür(yöne bağlı olarak)
        def koorYilanKafaSolCaprazDondur(yon):
            if yon == 1:    # sağ için
                return [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1] + 1]
            if yon == 2:    # aşağı için
                return [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1] + 1]
            if yon == 3:    # sol için
                return [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1] - 1]
            if yon == 4:    # yukarı için
                return [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1] - 1]
        
        # Yılanın kafasının sağ çaprazındaki koordinatları döndür(yöne bağlı olarak)
        def koorYilanKafaSagCaprazDondur(yon):
            if yon == 1:    # sağ için
                return [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1] + 1]
            if yon == 2:    # aşağı için
                return [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1] - 1]
            if yon == 3:    # sol için
                return [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1] - 1]
            if yon == 4:    # yukarı için
                return [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1] + 1]
        
        # "koor" dan, "koorYilanParcaKenarKose" içindeki listelerdeki koordinatlardan gitmek koşulu ile,
        # yılanın kuyruğunun herhangi bir köşe ya da kenarına gidilip gidilemediğini kontrol et
        def koorYilanKuyrugunaGiderMi(koor, koorYilanParcaKenarKose):
            return True
        
        
        
        for yon in self.gidilebilecekYonler:
            ## Eğer robot yılanın kafasının sol çapraz ve sağ çaprazındaki noktalardan(yöne bağlı),
            ## hep yılanın parçalarının yanından ya da köşesinden gitmek koşulu ile,
            ## herhangi bir şekilde kuyruğa erişilebiliyorsa o zaman çıkmaz
            ## sokağa girilmiyor demektir. Aksi halde bir çıkmaz sokağa giriliyor demektir.
            
            
            
            yeniGidilebilecekYonler = []
            if yon == 1:    # sağ için
                # yılanın parçalarının kenar ve köşe koordinatlarını bulma
                koorYilanParcaKenarKose = []    # kenar ve köşe koordinatlarını tutan liste
                # listeye yılan koordinatlarının sayısı kadar boş liste ekle
                for sayac in range(len(self.yilan.koordinatlarim)):
                    koorYilanParcaKenarKose.append([])
                # yılanın parçalarının kenar ve köşe koordinatlarını
                # listedeki listelere sırasıyla yazdır
                for sayac in range(len(self.yilan.koordinatlarim)):
                    koorYilanParcaKenarKose[sayac] = [[self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1]],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1]],
                                                      [self.yilan.koordinatlarim[sayac][0],
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0],
                                                       self.yilan.koordinatlarim[sayac][1] + 1],
                                                      [self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1] + 1],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1] + 1]]
                ## yılanın kafasının önündeki koordinatı listeden çıkar
                # yılanın kafasının ön koordinatını bul
                koorKafaOn = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] + 1]
                # bu koordinatı listedeki ilk listeden(kafayla ilgili olan) çıkar
                koorYilanParcaKenarKose[0].remove(koorKafaOn)
                
                # yılanın üstünde ve sahanın dışında olan koordinatları listedeki listelerden çıkar
                geciciListe1 = koorYilanParcaKenarKose[:]
                for listeSayaci in range(len(koorYilanParcaKenarKose)):
                    geciciListe2 = koorYilanParcaKenarKose[listeSayaci][:]
                    for koorSayaci in range(len(koorYilanParcaKenarKose[listeSayaci])):
                        if koorYilanUstundeMi(koorYilanParcaKenarKose[listeSayaci][koorSayaci]) == True or \
                           koorSahaDisindaMi(koorYilanParcaKenarKose[listeSayaci][koorSayaci]) == True:
                            geciciListe2.remove(koorYilanParcaKenarKose[listeSayaci][koorSayaci])
                    geciciListe1[listeSayaci] = geciciListe2
                koorYilanParcaKenarKose = geciciListe1
                
                ## yılanın sağ çapraz ve sol çapraz koordinatlarının yılanın kuyruğuna varıp varmadığını
                ## kontrol et
                # yılanın kafasının sol çapraz ve sağ çapraz tarafını bulma
                koorYilanKafaSolCapraz = koorYilanKafaSolCaprazDondur(yon)
                koorYilanKafaSagCapraz = koorYilanKafaSagCaprazDondur(yon)
                # yılanın kafasının sol çaprazı ve sağ çaprazı boş ise...
                if koorYilanUstundeMi(koorYilanKafaSolCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSolCapraz) == False and \
                   koorYilanUstundeMi(koorYilanKafaSagCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSagCapraz) == False:
                    # eğer sol çapraz ya da sağ çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSolCapraz,
                                                 koorYilanParcaKenarKose) == True or \
                       koorYilanKuyrugunaGiderMi(koorYilanKafaSagCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sol çaprazı boş ise...
                elif koorYilanUstundeMi(koorYilanKafaSolCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSolCapraz) == False:
                    # eğer sol çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSolCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sağ çaprazı boş ise...
                elif koorYilanUstundeMi(koorYilanKafaSagCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSagCapraz) == False:
                    # eğer sağ çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSagCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sol çaprazı ve sağ çaprazı boş değil ise...
                else:
                    pass    # geç
            
            
            
            
            
            if yon == 2:    # aşağı için
                # yılanın parçalarının kenar ve köşe koordinatlarını bulma
                koorYilanParcaKenarKose = []    # kenar ve köşe koordinatlarını tutan liste
                # listeye yılan koordinatlarının sayısı kadar boş liste ekle
                for sayac in range(len(self.yilan.koordinatlarim)):
                    koorYilanParcaKenarKose.append([])
                # yılanın parçalarının kenar ve köşe koordinatlarını listedeki listelere sırasıyla yazdır
                for sayac in range(len(self.yilan.koordinatlarim)):
                    koorYilanParcaKenarKose[sayac] = [[self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1]],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1]],
                                                      [self.yilan.koordinatlarim[sayac][0],
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0],
                                                       self.yilan.koordinatlarim[sayac][1] + 1],
                                                      [self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1] + 1],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1] + 1]]
                ## yılanın kafasının önündeki koordinatı listeden çıkar
                # yılanın kafasının ön koordinatını bul
                koorKafaOn = [self.yilan.koordinatlarim[0][0] + 1, self.yilan.koordinatlarim[0][1]]
                # bu koordinatı listedeki ilk listeden(kafayla ilgili olan) çıkar
                koorYilanParcaKenarKose[0].remove(koorKafaOn)
                
                # yılanın üstünde ve sahanın dışında olan koordinatları listedeki listelerden çıkar
                geciciListe1 = koorYilanParcaKenarKose[:]
                for listeSayaci in range(len(koorYilanParcaKenarKose)):
                    geciciListe2 = koorYilanParcaKenarKose[listeSayaci][:]
                    for koorSayaci in range(len(koorYilanParcaKenarKose[listeSayaci])):
                        if koorYilanUstundeMi(koorYilanParcaKenarKose[listeSayaci][koorSayaci]) == True or \
                           koorSahaDisindaMi(koorYilanParcaKenarKose[listeSayaci][koorSayaci]) == True:
                            geciciListe2.remove(koorYilanParcaKenarKose[listeSayaci][koorSayaci])
                    geciciListe1[listeSayaci] = geciciListe2
                koorYilanParcaKenarKose = geciciListe1
                
                ## yılanın sağ çapraz ve sol çapraz koordinatlarının yılanın kuyruğuna varıp varmadığını
                ## kontrol et
                # yılanın kafasının sol çapraz ve sağ çapraz tarafını bulma
                koorYilanKafaSolCapraz = koorYilanKafaSolCaprazDondur(yon)
                koorYilanKafaSagCapraz = koorYilanKafaSagCaprazDondur(yon)
                # yılanın kafasının sol çaprazı ve sağ çaprazı boş ise...
                if koorYilanUstundeMi(koorYilanKafaSolCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSolCapraz) == False and \
                   koorYilanUstundeMi(koorYilanKafaSagCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSagCapraz) == False:
                    # eğer sol çapraz ya da sağ çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSolCapraz,
                                                 koorYilanParcaKenarKose) == True or \
                       koorYilanKuyrugunaGiderMi(koorYilanKafaSagCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sol çaprazı boş ise...
                elif koorYilanUstundeMi(koorYilanKafaSolCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSolCapraz) == False:
                    # eğer sol çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSolCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sağ çaprazı boş ise...
                elif koorYilanUstundeMi(koorYilanKafaSagCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSagCapraz) == False:
                    # eğer sağ çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSagCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sol çaprazı ve sağ çaprazı boş değil ise...
                else:
                    pass    # geç
            
            
            
            
            
            if yon == 3:    # sol için
                # yılanın parçalarının kenar ve köşe koordinatlarını bulma
                koorYilanParcaKenarKose = []    # kenar ve köşe koordinatlarını tutan liste
                # listeye yılan koordinatlarının sayısı kadar boş liste ekle
                for sayac in range(len(self.yilan.koordinatlarim)):
                    koorYilanParcaKenarKose.append([])
                # yılanın parçalarının kenar ve köşe koordinatlarını listedeki listelere sırasıyla yazdır
                for sayac in range(len(self.yilan.koordinatlarim)):
                    koorYilanParcaKenarKose[sayac] = [[self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1]],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1]],
                                                      [self.yilan.koordinatlarim[sayac][0],
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0],
                                                       self.yilan.koordinatlarim[sayac][1] + 1],
                                                      [self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1] + 1],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1] + 1]]
                ## yılanın kafasının önündeki koordinatı listeden çıkar
                # yılanın kafasının ön koordinatını bul
                koorKafaOn = [self.yilan.koordinatlarim[0][0], self.yilan.koordinatlarim[0][1] - 1]
                # bu koordinatı listedeki ilk listeden(kafayla ilgili olan) çıkar
                koorYilanParcaKenarKose[0].remove(koorKafaOn)
                
                # yılanın üstünde ve sahanın dışında olan koordinatları listedeki listelerden çıkar
                geciciListe1 = koorYilanParcaKenarKose[:]
                for listeSayaci in range(len(koorYilanParcaKenarKose)):
                    geciciListe2 = koorYilanParcaKenarKose[listeSayaci][:]
                    for koorSayaci in range(len(koorYilanParcaKenarKose[listeSayaci])):
                        if koorYilanUstundeMi(koorYilanParcaKenarKose[listeSayaci][koorSayaci]) == True or \
                           koorSahaDisindaMi(koorYilanParcaKenarKose[listeSayaci][koorSayaci]) == True:
                            geciciListe2.remove(koorYilanParcaKenarKose[listeSayaci][koorSayaci])
                    geciciListe1[listeSayaci] = geciciListe2
                koorYilanParcaKenarKose = geciciListe1
                
                ## yılanın sağ çapraz ve sol çapraz koordinatlarının yılanın kuyruğuna varıp varmadığını
                ## kontrol et
                # yılanın kafasının sol çapraz ve sağ çapraz tarafını bulma
                koorYilanKafaSolCapraz = koorYilanKafaSolCaprazDondur(yon)
                koorYilanKafaSagCapraz = koorYilanKafaSagCaprazDondur(yon)
                # yılanın kafasının sol çaprazı ve sağ çaprazı boş ise...
                if koorYilanUstundeMi(koorYilanKafaSolCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSolCapraz) == False and \
                   koorYilanUstundeMi(koorYilanKafaSagCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSagCapraz) == False:
                    # eğer sol çapraz ya da sağ çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSolCapraz,
                                                 koorYilanParcaKenarKose) == True or \
                       koorYilanKuyrugunaGiderMi(koorYilanKafaSagCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sol çaprazı boş ise...
                elif koorYilanUstundeMi(koorYilanKafaSolCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSolCapraz) == False:
                    # eğer sol çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSolCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sağ çaprazı boş ise...
                elif koorYilanUstundeMi(koorYilanKafaSagCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSagCapraz) == False:
                    # eğer sağ çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSagCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sol çaprazı ve sağ çaprazı boş değil ise...
                else:
                    pass    # geç
            
            
            
            
            
            if yon == 4:    # yukarı için
                # yılanın parçalarının kenar ve köşe koordinatlarını bulma
                koorYilanParcaKenarKose = []    # kenar ve köşe koordinatlarını tutan liste
                # listeye yılan koordinatlarının sayısı kadar boş liste ekle
                for sayac in range(len(self.yilan.koordinatlarim)):
                    koorYilanParcaKenarKose.append([])
                # yılanın parçalarının kenar ve köşe koordinatlarını listedeki listelere sırasıyla yazdır
                for sayac in range(len(self.yilan.koordinatlarim)):
                    koorYilanParcaKenarKose[sayac] = [[self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1]],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1]],
                                                      [self.yilan.koordinatlarim[sayac][0],
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0],
                                                       self.yilan.koordinatlarim[sayac][1] + 1],
                                                      [self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0] - 1,
                                                       self.yilan.koordinatlarim[sayac][1] + 1],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1] - 1],
                                                      [self.yilan.koordinatlarim[sayac][0] + 1,
                                                       self.yilan.koordinatlarim[sayac][1] + 1]]
                ## yılanın kafasının önündeki koordinatı listeden çıkar
                # yılanın kafasının ön koordinatını bul
                koorKafaOn = [self.yilan.koordinatlarim[0][0] - 1, self.yilan.koordinatlarim[0][1]]
                # bu koordinatı listedeki ilk listeden(kafayla ilgili olan) çıkar
                koorYilanParcaKenarKose[0].remove(koorKafaOn)
                
                # yılanın üstünde ve sahanın dışında olan koordinatları listedeki listelerden çıkar
                geciciListe1 = koorYilanParcaKenarKose[:]
                for listeSayaci in range(len(koorYilanParcaKenarKose)):
                    geciciListe2 = koorYilanParcaKenarKose[listeSayaci][:]
                    for koorSayaci in range(len(koorYilanParcaKenarKose[listeSayaci])):
                        if koorYilanUstundeMi(koorYilanParcaKenarKose[listeSayaci][koorSayaci]) == True or \
                           koorSahaDisindaMi(koorYilanParcaKenarKose[listeSayaci][koorSayaci]) == True:
                            geciciListe2.remove(koorYilanParcaKenarKose[listeSayaci][koorSayaci])
                    geciciListe1[listeSayaci] = geciciListe2
                koorYilanParcaKenarKose = geciciListe1
                
                ## yılanın sağ çapraz ve sol çapraz koordinatlarının yılanın kuyruğuna varıp varmadığını
                ## kontrol et
                # yılanın kafasının sol çapraz ve sağ çapraz tarafını bulma
                koorYilanKafaSolCapraz = koorYilanKafaSolCaprazDondur(yon)
                koorYilanKafaSagCapraz = koorYilanKafaSagCaprazDondur(yon)
                # yılanın kafasının sol çaprazı ve sağ çaprazı boş ise...
                if koorYilanUstundeMi(koorYilanKafaSolCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSolCapraz) == False and \
                   koorYilanUstundeMi(koorYilanKafaSagCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSagCapraz) == False:
                    # eğer sol çapraz ya da sağ çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSolCapraz,
                                                 koorYilanParcaKenarKose) == True or \
                       koorYilanKuyrugunaGiderMi(koorYilanKafaSagCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sol çaprazı boş ise...
                elif koorYilanUstundeMi(koorYilanKafaSolCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSolCapraz) == False:
                    # eğer sol çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSolCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sağ çaprazı boş ise...
                elif koorYilanUstundeMi(koorYilanKafaSagCapraz) == False and \
                   koorSahaDisindaMi(koorYilanKafaSagCapraz) == False:
                    # eğer sağ çaprazdan yılanın kuyruğuna gidilebiliyorsa...
                    if koorYilanKuyrugunaGiderMi(koorYilanKafaSagCapraz,
                                                 koorYilanParcaKenarKose) == True:
                        yeniGidilebilecekYonler.append(yon)    # bu yönü yeni listeye ekle
                # yılanın kafasının sol çaprazı ve sağ çaprazı boş değil ise...
                else:
                    pass    # geç
        
        self.gidilebilecekYonler = yeniGidilebilecekYonler
        """