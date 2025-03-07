import re


def email_check(email):
    # E-posta adresi için düzenli ifade (regex)
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # E-posta adresinin kontrolü
    if re.match(pattern, email):
        print("Girilen e-posta adresi geçerli.")
    else:
        print("Girilen e-posta adresi geçersiz.")


# Kullanıcıdan e-posta adresini alma
user_email = input("Lütfen e-posta adresinizi girin: ")

# E-posta adresinin kontrol edilmesi
email_check(user_email)
