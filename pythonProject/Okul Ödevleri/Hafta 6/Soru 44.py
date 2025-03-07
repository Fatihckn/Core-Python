import re


def check_date_format(date):
    # Tarih biçimi için düzenli ifade
    date_regex = re.compile(r'^\d{2}/\d{2}/\d{4}$')

    # Tarih biçiminin kontrol edilmesi
    if not date_regex.match(date):
        return False, "Tarih belirli bir biçime uygun değil. (dd/mm/yyyy)"

    # Tarihin geçerliliğinin kontrol edilmesi
    day, month, year = map(int, date.split('/'))
    max_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Şubat ayındaki gün sayısının kontrolü (artık yıl için)
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        max_days[1] = 29

    if month < 1 or month > 12:
        return False, "Geçersiz ay değeri."
    if day < 1 or day > max_days[month - 1]:
        return False, "Geçersiz gün değeri."

    return True, "Geçerli tarih formatı ve değeri."


# Kullanıcıdan tarih alınması
date = input("Lütfen bir tarih girin (dd/mm/yyyy): ")

# Tarihin kontrol edilmesi
result, message = check_date_format(date)

# Sonucun ekrana yazdırılması
print(message)
