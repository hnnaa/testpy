# coding:utf-8
import Queue
import math
import threading
import time

import win32api
import os, sys
from collections import Iterable
from functools import reduce

g_test_list = []


def add_list(str):
    g_test_list.append(str)


# 关键字参数 py3
# def guanjianzi_param_2(name, *, city, ff):
#     print(name, city, ff)


# 尾递归优化
def fact(num, p):
    if num == 1:
        return p
    return fact(num - 1, num * p)


# 汉诺
def move(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
    else:
        move(n - 1, a, c, b)
        print(a, "-->", c)
        move(n - 1, b, a, c)


# 斐波那契数列 生成器
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1


# 杨辉三角 生成器
def triangles():
    a = [1]
    while True:
        yield a
        a = [([0] + a)[x] + (a + [0])[x] for x in range(len(a) + 1)]


def get_file_version(file_name):
    info = win32api.GetFileVersionInfo(file_name, os.sep)
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    version = '%d.%d.%d.%d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
    return version


def cal_crc(ptr, length):
    crc = 0
    for j in range(length):
        for k in range(8):
            if crc & 0x8000:
                crc *= 2
                crc ^= 0x1021
            else:
                crc *= 2
            if ptr[j] & (0x80 >> k):
                crc ^= 0x1021
        crc &= 0xFFFF
        print ("crc=" + str(crc))
    return hex(crc).upper()


ORDER_ID = 1


class Eo:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def get_order_id():
    global ORDER_ID
    with Eo():
        ORDER_ID += 1
        if ORDER_ID > 0xFFFF:
            ORDER_ID = 1
        return ORDER_ID


if __name__ == "__main__":
    # 切片
    ls = ["1", "2"]
    ls2 = ls[0:4]
    print(str(ls[0:2]))
    info1 = "11724   112 10032    S     899m 89.5   1 10.2 {.postoffice:rtc} com.reformer.pos\n"
    print(len(info1))
    alst = [x.strip(" ") for x in info1.split(" ") if x.strip(" ") != ""]
    stra = "cpu占用:%s=%s%%;" % (reduce(lambda x, y: x + " " + y, alst[8:]).strip('\n'), alst[7])
    info2 = "11724   921760K   40552K   17317K   13708K  com.reformer.postoffice:rtc\n"
    alst = [x.strip(" ") for x in info2.split(" ") if x.strip(" ") != ""]
    stra = "内存占用:%s=%s;" % (" ".join(alst[5:]).strip('\n'), alst[2])
    # 关键字参数
    # guanjianzi_param_2("对方", city=1, ff="d")
    # 迭代
    its = iter((1, 2, 3, 4))
    while True:
        try:
            print(next(its))
        except StopIteration:
            break
    print(fact(5, 1))
    move(3, "A", "B", "C")
    print(isinstance({1, 2, 3}, Iterable))
    print(isinstance((1, 2, 3), Iterable))
    for index, value in enumerate({"a", 1, 3, "d"}):
        print(index, value)
    l = [x * x for x in range(1, 11)]
    l2 = [x for x in l if x % 2 == 0]
    l3 = [x + y for x in l for y in l2]
    print(l3)
    print([d for d in os.listdir(".")])
    f = fib(9)
    print(type(f))
    for i in f:
        print(i)
    i = 0
    for f in triangles():
        print(f)
        i = i + 1
        if i > 10:
            break
    for i, value in enumerate(range(1, 10)):
        print("i=%d,value=%d" % (i, value))

    # get_file_version(r"C:\Users\Administrator\Downloads\FrankMonitordll.dll")
    add_list("d")
    print(g_test_list)

    # s = os.system(r'ping baidu.com')
    # print(s)

    tt1 = time.strptime("2020-08-27 02:30:30", "%Y-%m-%d %H:%M:%S")
    print(time.strftime("%H:%M:%S", tt1))

    q = Queue.Queue(10)
    try:
        q.get_nowait()
    except:
        print ("no get_nowait data")

    head = bytearray(2)
    head[0] = ord('D')
    head[1] = 43

    print (head[0], head[1])

    abcc = {x for x in range(10)}

    bts = bytearray(255)
    for ii in range(len(bts)):
        bts[ii] = ii
    ress = cal_crc(bts, len(bts))

    print (len("中国"))
    get_order_id()

    bb=bytearray('中国\x33\x34')
    print str([r for r in bb])
    c=str(bb)
    text = "余位" + "%04d" % 123
    def _m():
        pass

    print (type(_m))
