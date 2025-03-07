import re

def filter_files_by_extension(directory, extension):
    # Belirtilen dizindeki tüm dosyaların listelenmesi
    file_list = ['dosya1.txt', 'dosya2.txt', 'resim.png', 'veri.csv']  # Örnek dosya listesi, gerçek dizin yerine kullanılmalıdır

    # Belirtilen uzantıya sahip dosyaların ayıklanması
    pattern = r"\." + re.escape(extension) + r"$"
    filtered_files = [file for file in file_list if re.search(pattern, file)]

    return filtered_files

# Dosyaların bulunduğu dizin ve aranılan dosya uzantısı
directory = "belirli_dizin_yolu"
extension = ".txt"

# Dosyaların ayıklanması
filtered_files = filter_files_by_extension(directory, extension)

# Sonuçların ekrana yazdırılması
print("Belirtilen uzantıya sahip dosyalar:")
for file in filtered_files:
    print(file)
