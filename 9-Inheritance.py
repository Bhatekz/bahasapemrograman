class Plant():

    def __init__(self, nama, jenis_tanaman, jenis_akar):
        self.nama = nama
        self.jenis_tanaman = jenis_tanaman
        self.jenis_akar = jenis_akar

    def cek_nama_tanaman(self):
        print('Nama Tanaman:',self.nama,'\nJenis Tanaman:',self.jenis_tanaman,'\njenis Akar:',self.jenis_akar)

class Nama_Bunga(Plant):
    def Nama_Bunga(self):
        print('Nama Bunga : ')
        pass

Tanaman_1 = Nama_Bunga('Melati','Tanaman Hias','Serabut')
Tanaman_2 = Nama_Bunga('Anggrek','Tanaman Hias','Akar Serabut')
Tanaman_3 = Nama_Bunga('Mawar','Tanaman Hias','Akar Serabut')

Tanaman_1.cek_nama_tanaman()
Tanaman_2.cek_nama_tanaman()
Tanaman_3.cek_nama_tanaman()
