#!/usr/bin/sh
# coding:utf-8
import random
import time, threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# threading.local 是同一个线程拥有各自的全局变量
local_s = threading.local()


def t_do_add():
    local_s.num = 0
    while True:
        local_s.num += 1
        print(threading.current_thread().name, local_s.num)
        time.sleep(random.random())


def t_do_minus():
    local_s.num = 0
    while True:
        local_s.num -= 1
        print(threading.current_thread().name, local_s.num)
        time.sleep(random.random())


t1 = threading.Thread(target=t_do_add, name="t1")
t1.start()
t2 = threading.Thread(target=t_do_minus, name="t2")
t2.start()

t2.join()
threading.Semaphore


