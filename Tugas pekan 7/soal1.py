# Membaca input dari pengguna
nama_kendaraan = input("Nama kendaraan? (contoh: mobil, motor): ")
jenis_bensin = input("Jenis bensin? (Pertalite, Pertamax, Pertamax Turbo): ")
kota_tujuan = input("Kota yang dituju? (jakarta, Bekasi, Depok, Tangerang, Bogor): ")

# Mendefinisikan data jarak dan harga bensin
data_jarak = {
    "jakarta": 20,
    "Bekasi": 35.7,
    "Depok": 5,
    "Tangerang": 99,
    "Bogor": 120.6
}

data_bensin = {
    "Pertalite": {"harga": 10000, "jarak_tempuh": 12},
    "Pertamax": {"harga": 14000, "jarak_tempuh": 13},
    "Pertamax Turbo": {"harga": 17000, "jarak_tempuh": 13.5}
}

# Menghitung pemakaian bensin
jarak = data_jarak.get(kota_tujuan, 0)
jarak_tempuh = data_bensin[jenis_bensin]["jarak_tempuh"]
pemakaian_bensin = jarak / jarak_tempuh

# Menghitung total harga
harga_per_liter = data_bensin[jenis_bensin]["harga"]
total_harga = pemakaian_bensin * harga_per_liter

# Menampilkan output
print("\nOutput:")
print("Nama Kendaraan:", nama_kendaraan)
print("Jenis Bensin:", jenis_bensin)
print("Kota yang Dituju:", kota_tujuan)
print("Pemakaian Bensin:", pemakaian_bensin, "liter")
print("Total Harga dari Bensin:", total_harga, "rupiah")