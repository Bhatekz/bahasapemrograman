class Waktu:

    def __init__(self, jam, menit, detik):
        self.jam = jam
        self.menit = menit
        self.detik = detik
    
    def info(self):
        if self.jam >= 24 or self.menit >= 60 or self.detik >= 60:
            print("Input Salah !")
        else:
            print(self.jam,':',self.menit,':',self.detik)

Waktu = Waktu (int(input("Input Jam : ")) ,int(input("Input Menit : ")) ,int(input("Input Detik : ")))
Waktu.info() 