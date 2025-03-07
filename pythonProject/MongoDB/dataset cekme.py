from datasets import load_dataset
from pymongo import MongoClient

# Veri setini yükle
dataset = load_dataset("proj-persona/PersonaHub", "instruction")

# İlk birkaç örneği kontrol et
print(dataset)

# MongoDB'ye bağlan
client = MongoClient("mongodb://localhost:27017/")  # Burada bağlantı URL'sini kendi ayarlarına göre düzenle
db = client["persona_database"]  # Veri tabanı adını belirle
collection = db["persona_collection"]  # Koleksiyon adını belirle

# Her bir veriyi MongoDB koleksiyonuna ekle
for entry in dataset['train']:  # 'train' bölümü üzerinde çalıştığımızı varsayıyoruz
    collection.insert_one(entry)

print("Veri seti MongoDB'ye kaydedildi.")
