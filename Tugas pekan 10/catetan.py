# Array berisi sekumpulan data dengan urutan tertentu, bisa ada duplikasi. diakses dengan indeks
# List merupakan impelementasi dari array
# Stack (tumpukan), pengecekan tanda kurung, sistem undo redo
# Push menyimpan data ke atas, dan pop untuk mengambil data paling atas. contoh:
# contoh stack
bilangan = [1,2,3]
# Stack / tumpukan (LIFO)
# Push
bilangan.append(5)
print(bilangan)
# Pop /Mengambil data paling atas
bilangan.pop()
bilangan.pop()
print(bilangan)
# Queue artinya antrian, sturuktur data FIFO
# 2 perintah
queue = []
# Queue/antrian (LIFO), kegunaan queue yaitu membuat sistem antrian
# Menambah queue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
# mengeluarkan queue (dequeue)
queue.pop(0)
print(queue)
# Set berarti himpunan dan tidak ada duplikasi, dituliskan dengan kurung kurawal dan tidak ada jaminan urutan
# set
motor = {"Beat","Vario","Scoopy","Mio","Nmax","Nmax"}
mobil = {"Avanza","BMW"}
print(motor)
# untuk menambahkan dengan add
motor.add("Aerox")
print(motor)
# untuk menghapus item
motor.remove("Scoopy")
print(motor)
# Menggabungkan set(union)
kendaraan = motor.union(mobil)
print(kendaraan)
# update set
motor.update(mobil)
print(motor)
# Dictionary untuk menyimpan data yang diakses bukan dengan indeks, data disimpan sebagai pasangan key dan value, diapit dengan kurung kurawal dan dipisah dengan titik dua
# Dictionary
data_diri = {"nama":"Reza","mapel":"DDP"}
# Mengakses dictioinary
print(data_diri["nama"])
# Mengubah nilai
data_diri["nama"]="kim"
print(data_diri)
# Menambah data
data_diri["Jurusan"] = "Sistem Informasi"
print (data_diri)
# Menghapus data
data_diri.pop("mapel")
print(data_diri)
# cek keberadaan key
if "mapel" in data_diri:
    print("Terdapat mapel")  
else :
    print("Mapel tidak ada")
# list : berisi sekumpulan data dengan urutan tertentu, bisa ada duplikat
# implementasi lain : LinkedList
# tidak dapat diakses dengan indeks, memililki akses ke entri pertama
# Struktur data bertingkat : bisa ad list, dict di dalam list, dan sebagainya.
# Struktur data khas python
#list
#contoh
daftar_buah =['rambutan', 'jambu', 'mangga', 'pepaya', 'pisang']
print(daftar_buah[0:3])
print(daftar_buah[-1:2])
print(len(daftar_buah))
# Tuple
#berisi beberapa nilai, serupa list
#isi tuple tidak  bisa diubah
#dipisahkan koma, tidak harus dikurung oleh tanda kurung 
#contoh
zoo = ('python', 'elephant', 'penguin')
new_zoo = 'monkay', 'camel', zoo
print(new_zoo[2] [2])
#sequence : list, tuple, dan string sequence:
#contoh
buah2an = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
motor = ["Beat", "Vario", "Scoopy", "Mio", "Nmax"]
nama = "Siti Rizkiyah"
print(nama[5:-1])
if 'r' in nama:
    print("Ada!")
else:
    print("Tidak Ada.")
print(buah2an[::3])