#Buatlah sebuah program untuk membuat kalkulator sederhana dengan bahasa python dengan ketentuan sebagai berikut:

angka1 = int (input("masukkan angka pertama: "))
angka2 = int (input("masukkan angka kedua:"))
operator = input("masukkan operator yang digunakan")
if operator == "+":  
    hasil= angka1 + angka2
elif operator == "-":
    hasil= angka1 - angka2
elif operator == "*":
    hasil= angka1 * angka2
elif operator == "/":
    hasil= angka1 / angka2
elif operator == "**":
    hasil= angka1 ** angka2
print (hasil)
