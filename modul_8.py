import threading
import time
from modul_5 import words_in_str


def print_data(file_txt, num):
    for i in range(num):
        words_in_str(file_txt)
        time.sleep(2)


thread1 = threading.Thread(target=print_data, args=('text.txt', 10,))
thread2 = threading.Thread(target=print_data, args=('text1.txt', 10,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
