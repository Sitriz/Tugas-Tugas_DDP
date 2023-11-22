# 1. Buatlah fungsi untuk menampilkan data diri:
# Contoh pemanggilan : profil (nama,alamat, gender, umur,hoby)
def data_diri(nama,alamat, gender, umur,hoby)
print("Nama: ", nama)
print('Alamat: ',alamat)
print('Gender: ',gender)
print('Umur: ',umur)
print('Hoby: ',hoby)

#data_diri('kiya','pal','p','20','masak')

# 2.  buatlah fungsi untuk mencari kelulusan nilai dari ketentuan berikut:
#jika nilai < 60 maka gagal
#jika nilai = 61-70 maka baik
#jika nilai = 71-80 maka sangat baik
#jika nilai = 81-100 maka istimewa
def predikat_kelulusan(nilai):
    if nilai <60:
        print('gagal')
    elif nilai >= 61 and nilai <= 70:
        print('baik')
    elif nilai >= 71 and nilai <= 80:
        print('sangat baik')
    elif nilai >= 81 and nilai <= 100:
        print('istimewa')
predikat_kelulusan(80)





