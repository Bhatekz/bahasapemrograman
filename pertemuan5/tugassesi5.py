
from asyncore import ExitNow


barang  =[]
harga   =[]
total   =[]


while True:
    print(""" List Item     :\n
    1 . Baju    \t  100000
    2 . Celana  \t  120000
    3 . Topi    \t  50000
    4 . Sepatu  \t  200000
    5 . Kemeja  \t  180000
    """)
    

    kode = int(input("Masukkan Kode Barang  : "))
    if kode == 1:
        barang.append ("Baju")
        harga.append(100000)
        
    elif kode == 2:
        barang.append ("Celana")
        harga.append(120000)
        
    elif kode == 3:
        barang.append ("Topi")
        harga.append(50000)
        
    elif kode == 4:
        barang.append ("Sepatu")
        harga.append(200000)
        
    elif kode == 5:
        barang.append ("Kemeja")
        harga.append(180000)
    




    else:
        print("Kode Tidak Valid")

    lanjut = input("Lanjut Belanja  : Y / N : ")
    if lanjut=="Y" :
        print("Barang Selanjutnya :")
    elif lanjut=="N" :
        print("Transaksi Selesai")

        break