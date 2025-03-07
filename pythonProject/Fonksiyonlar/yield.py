# def karekok(liste):
#     yeni_liste = []
#     for i in liste:
#         i **=0.5
#         yeni_liste.append(i)
#     return yeni_liste
#
# for i in karekok([4,16,64]):
#     print(i)
# bu kod bir değerin işini sürekli beklediğinden büyük veri setlerinde verimsizdir.
def karekok(liste):
    for i in liste:
        yield i ** 0.5
# yield bir değerin işi bitince diğerlerinin bitmesini beklemeden direkt bastırır
liste = karekok([4,16,64])
for i in liste:
    print(i)

