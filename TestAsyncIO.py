# coding :utf-8
import threading
import time
from datetime import datetime
import platform


def num():
    a = yield 1
    print("a=", a)
    while True:
        a = yield a
        print("a=", a)


n = num()
print(n.send(None))
print(n.send(5))
print(n.send(50))

py_ver = platform.python_version()
print("py_ver=" + py_ver)
if py_ver.startswith("3"):
    import asyncio


    async def showa():
        print("hello a")
        await asyncio.sleep(1)
        print("hello a2")


    async def showb():
        print("hello b")
        await asyncio.sleep(0.5)
        print("hello b2")


    async def show():
        # print("hello start")
        await asyncio.sleep(5)
        # print("hello end")


    def show_th():
        # print("hello start")
        time.sleep(5)
        # print("hello end")


    t1 = datetime.now()
    loop = asyncio.get_event_loop()
    task = []
    for i in range(500):
        task.append(show())
    loop.run_until_complete(asyncio.wait(task))
    loop.close()
    print("use time=", datetime.now() - t1)

    time.sleep(1)
    t2 = datetime.now()
    ths = []
    for i in range(500):
        t = threading.Thread(target=show_th)
        ths.append(t)
        t.start()
    for th in ths:
        th.join()
    print("use time2=", datetime.now() - t2)
