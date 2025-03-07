from collections import defaultdict

dict = defaultdict(int)

cumle = 'fatih çokan ostim teknik üniversitesi'

for harf in cumle:
    if harf != ' ':
        dict[harf] += 1

for harf,frekans in dict.items():
    print(f"{harf} : {frekans}")
