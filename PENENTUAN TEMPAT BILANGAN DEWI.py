# Program Penentuan Nilai Tempat Bilangan

# Input dari pengguna
angka = input("Masukkan angka: ")

# Membuat daftar nama tempat nilai dari kanan ke kiri
tempat = ["satuan", "puluhan", "ratusan", "ribuan", "puluh ribuan",
          "ratus ribuan", "juta", "puluh juta", "ratus juta", "miliar"]

print(f"\nAnda memasukkan angka {angka} di mana:")

# Membalik angka agar mudah menyesuaikan tempat nilai
angka_terbalik = angka[::-1]

# Menampilkan nilai tempat
for i, digit in enumerate(angka_terbalik):
    if i < len(tempat):
        print(f"{digit} adalah {tempat[i]}")
    else:
        print(f"{digit} adalah nilai tempat lebih tinggi (di atas miliar)")