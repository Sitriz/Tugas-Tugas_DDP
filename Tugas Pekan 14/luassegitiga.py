#import modules
from tkinter import *
# buat tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# buat object root
root = ttk.Window(themename="morph")

# atur title aplikasi
root.title("Aplikasi Penghitung Luas Segitiga")

#atur lebar dan tinggi tampilan
root.geometry('400x250')

# buat teks
ttk.Label(root, text="Aplikasi penghitung luas segitiga", font=('calibri', 15, 'bold'), bootstyle=DARK).pack(pady=15)

ttk.Label(root, text="Masukkan alas").pack()

# buat kolom input
alas = Entry()
alas.insert(END, 0)
alas.pack()

ttk.Label(root, text="Masukkan tinggi").pack()

# buat kolom input
tinggi = Entry()
tinggi.insert(END, 0)
tinggi.pack()

def hitung():
    # tangkap inputtan user
    hasil_alas = int(alas.get())
    hasil_tinggi = int(tinggi.get())
    # hitung luas segitiga
    luas = 0.5 * hasil_alas * hasil_tinggi
    hasil = f"Hasil perhitungan luas segitiga: {luas}"
    #tambilkan hasil
    ttk.Label(root, text=hasil).pack()

# buat tombol hitung
ttk.Button(root, text="Hitung", command=hitung, bootstyle=PRIMARY).pack(pady=10)

# jalankan aplikasi
root.mainloop()