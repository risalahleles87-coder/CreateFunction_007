# TASK 1

import math


def konversi_suhu(nilai, satuan):
    if satuan == 'C':
        return (9/5 * nilai) + 32
    elif satuan == 'F':
        return (nilai - 32) * 5/9

suhu = float(input("Nilai suhu: "))
satuan = input("Satuan (C/F): ")
print("Hasil:", konversi_suhu(suhu, satuan))

# TASK 2
luas_lingkaran = lambda r: math.pi * r**2

r = float(input("Jari-jari (r): "))
print("Luas lingkaran:", luas_lingkaran(r))