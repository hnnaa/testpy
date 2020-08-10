# coding:utf-8
import os
import random
import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    QueueManager.register("get_task_queue")
    QueueManager.register("get_result_queue")

    m = QueueManager(address=("192.168.10.44", 7788), authkey=b"abc")
    m.connect()

    t_q = m.get_task_queue()
    r_q = m.get_result_queue()

    while True:
        t = t_q.get()
        time.sleep(random.random())
        print("task_get:%s" % str(t))
        r = "pid=%s,i=%s" % (os.getpid(), str(t))
        print("result_put:%s" % r)
        r_q.put(r)
        time.sleep(random.random())
