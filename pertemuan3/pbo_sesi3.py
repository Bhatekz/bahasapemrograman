print("Authorized by Bhatekz")

print("list daftar nilai mahasiswa")

nim=input("NIM :")
nama=input("Nama Mahasiswa :")
gender=input("Jenis Kelamin :")
date=input("Tanggal Input Nilai :")
matkul=input("Mata Kuliah :")
absen=input("Absensi :")
tugas=input("Tugas :")
uts=input("Nilai UTS :")
uas=input("Nilai UAS :")
na=int( tugas + uts + uas )/3


print("=======HASIL AKHIR========")

print("NIM :", nim)
print("Nama Mahasiswa :", nama)
print("Jenis Kelamin :", gender)
print("Tanggal Input Nilai :", date)
print("Mata Kuliah :", matkul)
print("Absensi :", absen)
print("Tugas :", tugas)
print("Nilai UTS :", uts)
print("Nilai UAS :", uas)
print("Nilai Akhir :", na)

if  na >= 80:
    print("Grade A")
    print("Keterangan : Lulus")
elif    na>=77:
    print("grade A-")
    print("Keterangan : Lulus")
elif    na >= 74:
    print("Grade B+")
    print("Keterangan : Lulus")
elif    na >= 71:
    print("Grade B")
    print("Keterangan : Lulus")
elif    na >= 68:
    print("Grade B-")
    print("Keterangan : Lulus")
elif    na >= 64:
    print("Grade C+")
    print("Keterangan : Lulus")

elif    na >= 60:
    print("Grade C")
    print("Keterangan : Tidak Lulus")

elif    na >= 50:
    print("Grade D")
    print("Keterangan : Tidak Lulus")

elif    na <= 49:
    print("Grade E")
    print("Keterangan : Tidak Lulus")
