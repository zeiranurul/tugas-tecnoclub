"""
Mencari Makanan di Hutan

Penduduk Pulau Tara meminta bantuanmu untuk menghitung berapa banyak buah yang ada di hutan. 
Mereka memiliki daftar jumlah buah yang ditemukan setiap hari selama seminggu, 
dan mereka butuh bantuanmu untuk mengetahui jumlah total buah yang dikumpulkan selama seminggu.

Contoh
Input:
[10, 20, 30, 40, 50, 60, 70]

Output:
Total buah yang dikumpulkan selama seminggu adalah 280
"""
buah = [10, 20, 30, 40, 50, 60, 70]

# lanjutkan code dibawah ini
buah = [10, 20, 30, 40, 50, 60, 70]
total_buah = 0
for jumlah in buah:
    total_buah += jumlah

print(f"Total buah yang dikumpulkan selama seminggu adalah {total_buah}")
