def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def kombinasi(n, r):
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# Contoh penggunaan
n = 5
r = 2
print("Kombinasi dari", n, "C", r, "adalah:", kombinasi(n, r))
