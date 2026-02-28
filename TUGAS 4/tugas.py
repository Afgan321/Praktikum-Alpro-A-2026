print("=== REGISTRASI PESERTA SEMINAR ===")

class NamaInvalidError(Exception):
    pass

class UmurInvalidError(Exception):
    pass

class EmailInvalidError(Exception):
    pass

class NomorInvalidError(Exception):
    pass


while True :
    try :
        nama = input(str('Nama: ' ))
        if len(nama) < 3 :
            raise NamaInvalidError()
        
        break

    except NamaInvalidError :
        print('[ERROR] Nama terlalu pendek! Minimal 3 karakter.')

    finally :
        pass

while True :
    try:
        umur = int(input('umur: ' ))
        if umur < 17 or umur > 60 :
            raise UmurInvalidError()
        
        break

    except UmurInvalidError :
            print('[ERROR] Umur tidak memenuhi Syarat')

    finally :
        pass

while True :
    try :
        email = str(input("Email: " ))
        if "@" not in email :
            raise EmailInvalidError()

        break

    except EmailInvalidError :
        print("[ERROR] Email tidak valid! Harus mengandung '@'.")

    finally :
        pass

while True :
    try :
        nomor = (input("No HP: "))
        if len(nomor) < 10 or len(nomor) > 13 or not nomor.isdigit():
            raise NomorInvalidError()

        print("Proses input selesai\n\n")
        break

    except NomorInvalidError :
        print("[ERROR] No HP tidak valid! Harus 10-13 digit angka.")

    finally :
        pass

print("=== DATA PESERTA ===")
print('Nama     : ', nama)
print("umur     : ", umur)
print("Email    : ", email)
print("No HP    : ", nomor)
print("Status   :  Terdaftar")

