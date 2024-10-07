"""
Menyusun Peta Harta Karun

Setelah berhasil membuka pintu gua, kamu menemukan petunjuk menuju harta karun. 
Namun, peta harta karun tersebut terdiri dari beberapa angka yang perlu diurutkan agar bisa menunjukkan arah yang benar. 
Penduduk Pulau Python meminta bantuanmu untuk mengurutkan daftar angka.

Contoh
Input:
[4, 2, 1, 3, 5]

Output:
[1, 2, 3, 4, 5]
"""
angka = [4, 2, 1, 3, 5]

# lanjutkan code dibawah ini
import numpy as np

angka = np.array([4, 2, 1, 3, 5])

# Mengurutkan angka menggunakan NumPy
hasil = np.sort(angka)

print(hasil.tolist())  
