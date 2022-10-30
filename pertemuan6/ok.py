import math as m
 
print("====================KONVERSI WAKTU====================")
try:
    totaldetik = int(input("Masukan jumlah detik: "))
    if totaldetik >= 359999:
        print("Invalid Input!")
    elif totaldetik >= 0:
        hh = m.floor(totaldetik / 3600)
        sisadetik = totaldetik % 3600
        mm = m.floor(sisadetik / 60)
        ss = sisadetik % 60
        print(f"{totaldetik} detik sama dengan {hh}:{mm}:{ss}")
    else:
        print("Invalid Input!")
except:
    print("Invalid Input!")
    