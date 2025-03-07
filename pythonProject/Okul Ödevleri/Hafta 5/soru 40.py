import os

klasor_yolu = "C:\\Program Files\\JetBrains"
with open("ödev8.txt","w",encoding = "utf-8") as file:
    for klasor, alt_klasorler, dosyalar in os.walk(klasor_yolu):
        file.write(f"Klasör: {klasor}\n")
        for dosya_adi in dosyalar:
            file.write(f"Dosya: {dosya_adi}\n")
        for alt_klasor in alt_klasorler:
            file.write(f"Alt Klasör: {os.path.join(klasor, alt_klasor)}\n")
        file.write("\n")