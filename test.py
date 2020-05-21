# coding:utf-8
import math
import os
from collections import Iterable


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


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1


def triangles():
    a = [1]
    while True:
        yield a
        a = [([0] + a)[x] + (a + [0])[x] for x in range(len(a)+1)]


if __name__ == "__main__":
    guanjianzi_param_2("对方", city=1, ff="d")
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