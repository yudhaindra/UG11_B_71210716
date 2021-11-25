nawal = str(input("Masukan kalimat awal : "))
nasip = str(input("Masukan kata untuk disisipkan : "))
hudex = int(input("Masukkan index : "))

sisip = nawal.find(nawal[hudex-1])

print(nawal[:sisip]+ nasip + nawal[sisip:])