from collections import defaultdict

"""dict = {}

dict[1] = 'a'
dict[2] = 'b'
dict[3] = 'c'

print(dict[4])
"""
# Yukarıda bastırılan anahtar olmadığı için KeyError hatası veriyor

dict = defaultdict(int)

dict[1] = 'a'
dict[2] = 'b'
dict[3] = 'c'

print(dict[4])

"""Bu fabrika fonksiyonu, eksik anahtar işlemleri sırasında çağrılır ve otomatik
olarak varsayılan (default) bir değer oluşturur.
"""

dict_copy = dict.copy()
print(dict_copy)