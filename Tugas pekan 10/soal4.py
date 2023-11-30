# Soal No. 4
def konsonan_saja(string_input):
    konsonan = [char for char in string_input if char.isalpha() and char.lower() not in ['a', 'e', 'i', 'o', 'u']]
    return ''.join(konsonan)
hasil_konsonan = konsonan_saja("Nurul Fikri")
print("Hasilnya Konsonan:", hasil_konsonan)