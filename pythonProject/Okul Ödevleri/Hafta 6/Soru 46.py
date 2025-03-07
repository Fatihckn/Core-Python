import re

def remove_html_tags(html):
    clean_text = re.sub(r'<.*?>', '', html)  # Tüm HTML etiketlerini kaldırır
    return clean_text

html_input = input("Lütfen HTML metnini girin: ")
clean_text = remove_html_tags(html_input)
print("HTML etiketleri kaldırılmış metin:")
print(clean_text)
