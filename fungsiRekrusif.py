def is_prima(n, i=2):
    if n <= 1:
        return False

    if i == n:
        return True

    if n % i == 0:
        return False

    return is_prima(n, i + 1)

angka = 15

if is_prima(angka):
    print(angka, "adalah bilangan prima")
else:
    print(angka, "bukan bilangan prima")
