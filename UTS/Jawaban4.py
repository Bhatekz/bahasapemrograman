
from asyncore import ExitNow


barang  =[]
harga   =[]
ppn     =[]
total   =[]


while True:
    print(""" List Item     :\n
    1 . Baju    \t  100000
    2 . Celana  \t  120000
    3 . Topi    \t  50000
    """)
    

    kode = int(input("Masukkan Kode Barang  : "))
    if  kode    == 1:
        barang  = ("Baju")
        harga   = (100000)
        ppn     =print("PPN 10%")
        total.append((harga*0.1)+harga)
        print("Total Harga : ",total)

    elif kode   == 2:
        barang  = ("Celana")
        harga   = (120000)
        ppn     = ("PPN 10%")
        total.append((harga*0.1)+harga)
        print("Total Harga :",total)

    elif kode == 3:
        barang  = ("Topi")
        harga   = (50000)
        ppn     = ("PPN 10%")
        total.append((harga*0.1)+harga)
        print("Total Harga :",total)

    else:
        print("kode tidak valid")


    lanjut = input("Lanjut Belanja  : Y / N : ")
    if  lanjut=="Y":
        print("Barang Selanjutnya :")

        
    elif lanjut=="N":
        print("Transaksi Selesai")
        print("Terima Kasih")
        break