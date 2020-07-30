# coding:utf-8
import math
import win32api
import os
from collections import Iterable


# 关键字参数
def guanjianzi_param_2(name, *, city, ff):
    print(name, city, ff)


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


if __name__ == "__main__":
    guanjianzi_param_2("对方", city=1, ff="d")
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
    for i, value in enumerate(range(1,10)):
        print("i=%d,value=%d" % (i, value))

    get_file_version(r"C:\Users\Administrator\Downloads\FrankMonitordll.dll")
