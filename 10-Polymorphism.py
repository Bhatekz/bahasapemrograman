#Nama : Hendrycko Panjaitan
#Nim  : 20210801308


class garden :
    pass

class Anggrek :
    def Menanam(self):
        return 'Berhasil Menanam Anggrek'

class Mawar :
    def Menanam(self):
        return 'Berhasil Menanam Mawar'

class Melati :
    def Menanam(self):
        return 'Berhasil Menanam Melati'


Tanam_Anggrek = Anggrek()
Tanam_Mawar= Mawar()
Tanam_Melati = Melati()

for Tanaman in [Tanam_Anggrek , Tanam_Mawar , Tanam_Melati]:
    print(Tanaman.Menanam())