def is_palindrom(teks):
    teks = teks.lower().replace(" ", "")
    
    if len(teks) <= 1:
        return True

    if teks[0] != teks[-1]:
        return False

    return is_palindrom(teks[1:-1])

kalimat = "Ini bukan"

if is_palindrom(kalimat):
    print("Kalimat tersebut adalah palindrom")
else:
    print("Kalimat tersebut bukan palindrom")
