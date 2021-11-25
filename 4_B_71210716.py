a = str(input("Masukkan kalimat untuk dihitung : "))

def hitung():
    kalimat = len(a)
    hasil = kalimat * 2/3
    return hasil

kata = hitung()
print(int(kata))