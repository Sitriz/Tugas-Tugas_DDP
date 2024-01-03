class manusia :
    def __init__(self, fnama, lname):
        self.fnama = fnama 
        self.lname = lname

    def cetak (self):
        print("nama saya", self.fnama, self.lname)

class staff(manusia) :
    def bekerja (self) :
        print("saya pekerja keras")

class pelajar(manusia) :
    def __init__(self, fnama, lname, prodi, angkatan):
        super().__init__(fnama, lname)
        self.prodi = prodi
        self.angkatan = angkatan

    def cetak(self):
        super().cetak()
        print("saya mahasiswa angkatan", self.angkatan, self.prodi)

    def belajar(self):
        print("saya adalah pelajar")


# objek manusia
x = manusia("Nada", "Indah")
x.cetak()

# objek staff
y = staff("Dedi", "Drajat")
y.cetak()
y.bekerja()

# objek pelajar
danu = pelajar("danu", "setiawan", "Sistem Informasi", 2023)
danu.cetak()
danu.belajar()