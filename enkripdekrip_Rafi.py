import string

text = string.printable

def encrypt(isi):
    global text

    key = int(input('Masukkan Kunci : '))
    cipher = ''
    for i in isi:
        if i in text:
            k = text.find(i)
            k = (k + key)%100
            cipher = cipher+text[k]
        else:
            cipher = cipher + i

    return cipher

def decrypt(cipher):
    global text
    key = int(input('Masukkan Kunci : '))

    isi = ''
    for i in cipher:
        if i in text:
            k = text.find(i)
            k = (k - key)%100
            isi = isi + text[k]
        else:
            isi = isi + i

    return isi

if __name__ == '__main__':
    print('|========================================================|')
    print('                 Nama : Rafi Izzaturohman')
    print('                 Siswa SMK Yadika Soreang')
    print('                  Bootcamp PT.Hashmicro')
    print('|========================================================|')
    print(' Program Sederhana Enkripsi & Dekripsi Menggunakan Python')
    mode = int(input('1. Enkripsi\n2. Dekripsi\n===================================================\nPilih mode : '))

    if mode == 1:
        isi = input('Masukkan isi : ')
        print(encrypt(isi))
    elif mode == 2:
        cipher = input('Masukkan isi : ')
        print(decrypt(cipher))
    else:
        print('Pilih 1. Enkripsi atau 2. Dekripsi')