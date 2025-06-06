def faktorial(n):
    if n <= 1:
        return 1
    return n * faktorial(n - 1)

def jumlah_pola(angka=1, tambah=2, batas=1):
    if angka > batas:
        return 0
    return angka + jumlah_pola(angka + tambah, tambah + 2, batas)

n = 7
batas = faktorial(n)
hasil = jumlah_pola(angka=1, tambah=2, batas=batas)

print("n =", n)
print("n! =", batas)
print("Jumlah deret 1 + 3 + 7 + ... hingga n! adalah:", hasil)
