import re

def check_password(password):
    # Şifre güvenlik kriterlerini tanımlama
    min_length = 8
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'[0-9]')
    special_char_regex = re.compile(r'[!@#$%^&*()-=_+`~[\]{}|;:,.<>?]')

    # Şifrenin uzunluğunun kontrolü
    if len(password) < min_length:
        return False, "Şifre en az {} karakter uzunluğunda olmalıdır.".format(min_length)

    # Şifrede büyük harf kontrolü
    if not uppercase_regex.search(password):
        return False, "Şifre en az bir büyük harf içermelidir."

    # Şifrede küçük harf kontrolü
    if not lowercase_regex.search(password):
        return False, "Şifre en az bir küçük harf içermelidir."

    # Şifrede rakam kontrolü
    if not digit_regex.search(password):
        return False, "Şifre en az bir rakam içermelidir."

    # Şifrede özel karakter kontrolü
    if not special_char_regex.search(password):
        return False, "Şifre en az bir özel karakter içermelidir."

    # Tüm kriterler sağlanıyorsa
    return True, "Şifre güvenlik kriterlerini sağlıyor."

# Kullanıcıdan şifre alınması
password = input("Lütfen bir şifre girin: ")

# Şifrenin kontrol edilmesi
result, message = check_password(password)

# Sonucun ekrana yazdırılması
print(message)
