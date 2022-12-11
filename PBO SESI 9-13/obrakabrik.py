#Sesi 9
#INHERITANCE
      
      
        # Super class
class Plant(object):
    
    def __init__(self, JumlahAir, JumlahPupuk, StatusTumbuh):
        self.JumlahAir = JumlahAir
        self.JumlahPupuk = JumlahPupuk
        self.StatusTumbuh = StatusTumbuh

    def Tumbuh(self):
        if  self.StatusTumbuh > 3:
            self.JumlahAir ==2
            self.JumlahPupuk ==2
            self.StatusTumbuh ==4

    def cekKondisiTumbuh(self):
        if  self.JumlahAir >= 2 and self.JumlahPupuk >= 2:
            Plant.Tumbuh()
    
    def BeriAir(self):
        self.JumlahAir ==2
        Plant.cekKondisiTumbuh()
    
    def BeriPupuk(self):
        self.JumlahPupuk ==2
        Plant.cekKondisiTumbuh()
    
    def getStatusTumbuhText(self):
        if self.StatusTumbuh == 0:
            print("Benih Tanaman") 
        elif self.StatusTumbuh == 1:
            print("Tunas Tanaman")
        elif self.StatusTumbuh == 2:
            print("Kuncup Tanaman")
        elif self.StatusTumbuh == 3:
            print("Tanaman Dewasa")
        else:
            print("Berbunga")

    def DisplayPlant(self):
        
        print("Jumlah Air \t: {} \nJumlah Pupuk \t: {}".format(self.JumlahAir, self.JumlahPupuk))

    def getJumlahAir(self):
        return self.JumlahAir
    
    def setJumlahAir(self, X):
        self.JumlahAir = X
    
    def getJumlahPupuk(self):
        return self.JumlahPupuk
    
    def setJumlahPupuk(self, X):
        self.JumlahPupuk = X
    
    def getStatusTumbuh(self):
        return self.StatusTumbuh
    
    def setStatusTumbuh(self, X):
        self.StatusTumbuh = X

        # Sub class
class Anggrek(Plant):

    def __init__(self, JumlahAir, JumlahPupuk, StatusTumbuh, Jenis):
        self.Jenis = Jenis
        Plant.__init__(self, JumlahAir, JumlahPupuk, StatusTumbuh)
    
    def anggrekTumbuh(self):
        if  self.StatusTumbuh == 4:
            self.JumlahAir += 2
            self.JumlahPupuk += 2
            self.StatusTumbuh == 4
    
    def cekKondisiTumbuh(self):
        if self.JumlahAir == 2 and self.JumlahPupuk == 2:
            Anggrek.anggrekTumbuh()
    
    def getJenis(self):
        return self.Jenis

        # Sub class
class Mawar(Plant):

    def __init__(self, JumlahAir, JumlahPupuk, StatusTumbuh, Jenis):
        self.Jenis = Jenis
        Plant.__init__(self, JumlahAir, JumlahPupuk, StatusTumbuh)
    
    def mawarTumbuh(self):
        if self.StatusTumbuh > 4:
            self.JumlahAir +=3
            self.JumlahPupuk += 2
            self.StatusTumbuh == 5
    
    def cekKondisiTumbuh(self):
        if self.JumlahAir == 3 and self.JumlahPupuk == 2:
            Mawar.mawarTumbuh()
    
    def getJenis(self):
        return self.Jenis
 
        # Sub class
class Melati(Plant):

    def __init__(self, JumlahAir, JumlahPupuk, StatusTumbuh, Jenis):
        self.Jenis = Jenis
        Plant.__init__(self, JumlahAir, JumlahPupuk, StatusTumbuh)
    
    def melatiTumbuh(self):
        if self.StatusTumbuh < 4:
            self.JumlahAir += 2
            self.JumlahPupuk += 1
            self.StatusTumbuh == 3
    
    def cekKondisiTumbuh(self):
        if self.JumlahAir == 2 and self.JumlahPupuk == 1:
            Melati.melatiTumbuh()
    
    def getJenis(self):
        return self.Jenis
 


Tanaman1 = Anggrek(2, 2, 4, 'Anggrek')
print("Jenis Tanaman \t: {}".format(Tanaman1.Jenis))
Tanaman1.getStatusTumbuhText()
Tanaman1.DisplayPlant()

Tanaman2 = Mawar(3, 2, 5, 'Mawar')
print("\nJenis Tanaman \t: {}".format(Tanaman2.Jenis))
Tanaman2.getStatusTumbuhText()
Tanaman2.DisplayPlant()

Tanaman3 = Melati(2, 1, 3, 'Melati')
print("\nJenis Tanaman \t: {}".format(Tanaman3.Jenis))
Tanaman3.getStatusTumbuhText()
Tanaman3.DisplayPlant()



#Sesi 10 
# POLYMORPHISM

class Garden (Plant):

    def __init__(self,JumlahAir, JumlahPupuk, StatusTumbuh, Size, nTanaman, mGarden, HasilPanen):
        self.size = Size
        self.nTanaman = nTanaman
        self.mGarden = mGarden
        self.pArrList = [" "]
        self.HasilPanen = HasilPanen
        Plant.__init__(self, JumlahAir,JumlahPupuk, StatusTumbuh)

    def Garden(self,pName):
        self.mGarden = pName

    def addPlant(self):
        if self.nTanaman < self.size:
            self.pArrList.append()
            self.nTanaman +=1
            return True
        else:
            return False


    def HarvestPlant(self):
        tmpN = 0
        i = 0
        Length = len(self.pArrList)
        while   self.pArrList != 0 and i < Length:
            if  self.pArrList[i] == 4 and Plant.getStatusTumbuh() == 4:
                self.pArrList.remove[i]
                self.nTanaman -=1
                tmpN -= 1
                i = 0
            else:
                i += 1

                self.HasilPanen = self.HasilPanen + (tmpN*100)
                return tmpN

    def BeriAir(self):
        for i in range(0, len(self.pArrList)):
            self.pArrList[i] = Garden.BeriAir()

    def BeriPupuk(self):        
        for i in range(0, len(self.pArrList)-1):
            self.pArrList[i] = Garden.BeriPupuk()

    def DisplayPlant(self):
        print(".....{}".format(self.mGarden))
        print("There are {} Plant In the Garden".format(self.nTanaman))
        print("Your Harvest Point : {}".format(self.HasilPanen))

        for i in range(0, len(self.pArrList)-1):
            self.pArrList[i] = Garden.DisplayPlant()

    def getHasilPanen(self):
        return self.HasilPanen