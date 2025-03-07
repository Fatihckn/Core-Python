"""
- threading.get_indent() metotuyla threading kimliğini elde ederiz.
- her iş parçacığının kimliği birbirinden farklıdır.
"""

import threading


def my_function():
    thread_id = threading.get_ident()

    print(f"Bu iş parçacığının kimliği: {thread_id}")



thread = threading.Thread(target=my_function)
thread.start()

thread2 = threading.Thread(target=my_function)
thread2.start()

