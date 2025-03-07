import threading
# global değişken x
x = 0

def artir():
	"""
	x global değişkenini artırmak için fonksiyon
	"""
	global x
	x += 1
def is_parcalari_gorevi():
	"""
	iş parçacığı görevi
	100000 kez artir fonksiyonunu çağırır.
	"""
	for _ in range(100000):
		artir()
def ana_gorev():
	global x
	# global değişken x'i 0 olarak ayarla
	x = 0

	# iş parçacıklarını oluştur
	t1 = threading.Thread(target=is_parcalari_gorevi)
	t2 = threading.Thread(target=is_parcalari_gorevi)

	# iş parçacıklarını başlat
	t1.start()
	t2.start()

	# iş parçacıklarının işlerini bitirmesini bekle
	t1.join()
	t2.join()

if __name__ == "__main__":
	for i in range(10):
		ana_gorev()
		print("İterasyon {0}: x = {1}".format(i,x))

