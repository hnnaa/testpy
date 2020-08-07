#!/usr/bin/sh
# coding:utf-8

import os
import random
import subprocess
import time
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue

'''
# 仅限linux
print('process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

while True:
    time.sleep(1)
'''


# 多进程

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# 进程池
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def q_put(q):
    for i in range(5):
        q.put(i)
        print("pid=%s q put:%s" % (os.getpid(), str(i)))
        time.sleep(random.random())


def q_get(q):
    while True:
        data = q.get(True)
        print("pid=%s q get:%s" % (os.getpid(), data))


if __name__ == '__main__':
    print("Parent Process is %s" % os.getpid())
    p = Process(target=run_proc, args=('test',))
    p.start()
    p.join()
    # Pool
    print('Parent process %s.' % os.getpid())
    pl = Pool()
    for i in range(5):
        pl.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    pl.close()  # 先关闭，停止添加子进程
    pl.join()  # 等待
    print('All subprocesses done.')
    # 子进程subprocess
    r = subprocess.call(["ping", "baidu.com"])
    print(r)
    '''
    # 如果子进程还需要输入，则可以通过communicate()方法输入：
    sp = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = sp.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', sp.returncode)
    '''
    # 进程间通信
    print("current pid=%s" % os.getpid())
    q = Queue()
    qw = Process(target=q_put, args=(q,))
    qr = Process(target=q_get, args=(q,))
    qw.start()
    qr.start()
    # qw.join()
    # qw.terminate()  # 强行终止
