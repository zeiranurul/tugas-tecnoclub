"""
Menyeberangi Jembatan Gantung

Setelah membantu penduduk dengan makanan, mereka mengizinkanmu melintasi jembatan gantung. 
Namun, jembatan ini sangat rapuh. Hanya orang-orang dengan berat badan tertentu yang boleh menyeberang. 
Kamu harus menulis program untuk menentukan apakah kamu bisa menyeberang jembatan.

Contoh 1
Input:
weight = 50

Output:
Kamu tidak boleh menyeberang jembatan

Contoh 2
Input:
weight = 90

Output:
Kamu boleh menyeberang jembatan
"""
weight = 90
# lanjutkan code dibawah ini
def bisa_menyeberang(weight):
    batas_berat_min = 50
    batas_berat_max = 100
    
    if weight < batas_berat_min or weight > batas_berat_max:
        return "Kamu tidak boleh menyeberang jembatan"
    else:
        return "Kamu boleh menyeberang jembatan"

weight = 90
print(bisa_menyeberang(weight))
