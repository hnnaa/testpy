# coding:utf-8
import time
from multiprocessing.managers import BaseManager
import queue

task_queue = queue.Queue()
result_queue = queue.Queue()


def method_task_queue():
    return task_queue


def method_result_queue():
    return result_queue


class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    QueueManager.register("get_task_queue", callable=method_task_queue)
    QueueManager.register("get_result_queue", callable=method_result_queue)

    m = QueueManager(address=("192.168.10.44", 7788), authkey=b"abc")
    m.start()

    t_q = m.get_task_queue()
    r_q = m.get_result_queue()

    for i in range(1000):
        t_q.put(i)
        print("task_put:%d" % i)

    while True:
        r = r_q.get()
        print("result_get:%s" % str(r))
