def jumlah_digit(n):
    if n < 10:
        return n
    return n % 10 + jumlah_digit(n // 10)

angka = 234
hasil = jumlah_digit(angka)
print("Jumlah digit dari", angka, "adalah:", hasil)
