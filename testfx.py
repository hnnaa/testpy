# coding:utf-8

# reduce() and map()
import sys
from functools import reduce
import testzhuangshiqi

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

buf = {}


def combine(x, y):
    return x * 10 + y


def str2int(s):
    return DIGITS[s]


def str2float(s):
    if "." not in s:
        s += ".0"
    index = s.index(".")
    return reduce(lambda x, y: 10 * x + y, map(lambda x: DIGITS[x], s[0: index])) \
           + reduce(lambda x, y: 0.1 * x + y, map(lambda x: DIGITS[x], (s[index + 1:][::-1] + "0")))


def log(func):
    def func_wrapper(a, b):
        print("call:" + func.__name__)
        return func(a, b)

    return func_wrapper


def zs(a, b):
    def func_wrapper(func):
        global buf
        buf[a + "_" + b] = func
        return func

    return func_wrapper


@log
def sum_a_b(a, b):
    return a + b


if __name__ == "__main__":
    # 高阶函数：map、reduce、filter
    print(reduce(combine, map(str2int, "1231231")))
    print(reduce(lambda x, y: 10 * x + y, map(lambda x: DIGITS[x], "12321313123")))
    print('str2float(\'123\') =', str2float('123'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
    # 反序
    print(str(1012)[::-1])
    # 装饰器
    print(sum_a_b(0.1, 0.2))
