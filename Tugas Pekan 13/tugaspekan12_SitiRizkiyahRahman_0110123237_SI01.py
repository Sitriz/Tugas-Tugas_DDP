# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak) buat minimal 3 class child (badak, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method
 
class Animal:
    def __init__(self, name, makanan, hidup, kembangBiak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.kembangBiak = kembangBiak

    def cetak(self):
        print(
            "Nama \t \t :", self.name,
            "\nMakanan \t :", self.makanan,
            "\nHidup \t \t :", self.hidup,
            "\nKembang Biak \t :", self.kembangBiak
        )


class Badak(Animal):
    def __init__(self, name, makanan, hidup, kembangBiak, umur, gender):
        super().__init__(name, makanan, hidup, kembangBiak)
        self.umur = umur
        self.gender = gender

    def cetak(self):
        super().cetak()
        print(
            "Umur \t \t :", self.umur,
            "\nGender \t \t :", self.gender,
            "\n-------------------------------"
        )


class Ikan(Animal):
    def __init__(self, name, makanan, hidup, kembangBiak, jumlah, jenis):
        super().__init__(name, makanan, hidup, kembangBiak)
        self.jumlah = jumlah
        self.jenis = jenis

    def cetak(self):
        super().cetak()
        print(
            "Jumlah \t \t :", self.jumlah,
            "\nJenis \t \t :", self.jenis,
            "\n-------------------------------"
        )


class Ular(Animal):
    def __init__(self, name, makanan, hidup, kembangBiak, ukuran, berbisa):
        super().__init__(name, makanan, hidup, kembangBiak)
        self.ukuran = ukuran
        self.berbisa = berbisa

    def cetak(self):
        super().cetak()
        print(
            "Ukuran \t \t :", self.ukuran,
            "\nBerbisa \t :", self.berbisa,
            "\n-------------------------------"
        )


badak = Badak("Azra", "Rumput", "Daratan", "Melahirkan", "30 tahun", "Betina")
ikan = Ikan("Ucul", "Makanan Ikan", "Air", "Bertelur", "18 Ekor", "Koi")
ular = Ular("Uler", "Ayam", "Alam Bebas", "Bertelur", "5 Meter", "Iya")

badak.cetak()
ikan.cetak()
ular.cetak()