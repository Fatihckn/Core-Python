"""
- current_thread() metotuyla aktif thread döndürülür.
"""
import threading

def my_function():
    print("Hello World!")




su_anki_thread = threading.current_thread()
print(f"Şu anki çalışan iş parçacığı: {su_anki_thread.name}")








