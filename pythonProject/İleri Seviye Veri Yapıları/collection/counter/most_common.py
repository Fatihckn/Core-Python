from collections import Counter

c = Counter('abcdeabcdabcaba')

print(c.most_common(3)) # en çok tekrar eden 3 harfi ve tekrar sayılarını bastırıyor

c.update('aaabbb') # yeni harfler ekliyor ve adetlerini ona göre güncelliyor
print(c.most_common(3))