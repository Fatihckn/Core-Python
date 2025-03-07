import threading
import time

class DataCampThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print('Starting Thread:', self.name)
        for i in range(3):  # 3 kez döngüye girerek işlem yapacak
            print(f'{self.name} --------> {time.time()}')
            time.sleep(self.delay)
        print('Execution of Thread:', self.name, 'is complete!')

# Thread nesnelerini oluşturma
t1 = DataCampThread('t1', 1)
t2 = DataCampThread('t2', 3)

# Thread'leri başlatma
t1.start()
t2.start()

# Thread'lerin tamamlanmasını bekler
t1.join()
t2.join()

print("Thread execution is complete!")
