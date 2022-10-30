# Konversi detik ke dalam jam menit dan detik

nilai = input("Masukkan Detik : ")
satuan = 60
detik = int(nilai)

hari = int(detik / (satuan * satuan * 24))
detik = int(detik - (satuan * satuan * 24) * hari)

jam = int(detik / (satuan * satuan))
detik = int(detik - (satuan * satuan) * jam)

menit = int(detik / satuan)
detik = int(detik - (satuan * menit))

print(f" Hari:Jam:Menit:Detik => {hari}:{jam}:{menit}:{detik}")
