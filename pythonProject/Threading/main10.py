"""
- Timer ile, bir threading başlamadan kaç saniye geçmesi gerektiğini
bildirebiliriz.
Timer sınıfı Thread sınıfının bir alt sınıfıdır. 
Dolayısıyla da Thread metotları burda da kullanılmaktadır.
"""

import threading


def selam_ver():
    print("Hello World!")



timer = threading.Timer(5,selam_ver)

timer.start()

