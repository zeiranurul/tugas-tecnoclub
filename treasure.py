"""
Mengungkap Pesan Tersembunyi

Di akhir petualangan, kamu menemukan kotak harta karun. 
Namun, untuk membukanya, kamu harus menemukan pesan tersembunyi di antara serangkaian kata. 
Penduduk Pulau Python memberimu sebuah daftar kata, dan kamu harus mencari kata yang paling sering muncul.

Contoh Input:
["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan"]

Contoh Output:
Kata yang paling sering muncul adalah "harta"
"""
arr = ["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan", "harta"]
# lanjutkan code dibawah ini
import pandas as pd

arr = ["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan", "harta"]

series = pd.Series(arr)
most_common_word = series.value_counts().idxmax()

print(f'Kata yang paling sering muncul adalah "{most_common_word}"')
