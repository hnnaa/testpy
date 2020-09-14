# coding :utf-8
import threading
from datetime import datetime
import time


def run(name):
    for i in range(600):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "hello", name)
        time.sleep(1)


t = threading.Thread(target=run, args=("abc",))
t.setDaemon(True)
t.start()
t2 = threading.Thread(target=run, args=("fff",))
t2.setDaemon(True)
t2.start()
t.join()
