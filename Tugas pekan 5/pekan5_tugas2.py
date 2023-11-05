print("""
    *** PILIH OPERASI ***
    1. HITUNG PERSEGI
    2. HITUNG LINGKARAN
    3. HITUNG SEGITIGA
    """)
pilihan = input("masukan pilihan: ")
match pilihan:
    case "1":
        s = int(input ("masukkan sisi:"))
        persegi = s*s
        print("luas persegi",persegi)
    case "2":
        phi = 3.14
        r = int(input ("masukkan jari:"))
        lingkaran = phi*r*r
        print("luas lingkaran",lingkaran)
    case "3":
        l = 1/2
        a = int(input ("masukkan alas:"))
        t = int(input ("masukkan tinggi:"))
        segitiga = l*a*t
        print("luas segitiga",segitiga)
    case _:
        print("pilihan tidak ada")