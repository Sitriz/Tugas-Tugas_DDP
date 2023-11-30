# Soal No. 3
def duplikasi(list_buah):
    buah_terduplikasi = []
    for buah in list_buah:
        buah_terduplikasi.append(buah)
        buah_terduplikasi.append(buah)
    return buah_terduplikasi
hasil_duplikasi = duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])
print("Hasilnya Duplikat:", hasil_duplikasi)