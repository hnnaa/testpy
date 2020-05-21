# coding:utf-8

# reduce() and map()
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def combine(x, y):
    return x * 10 + y


def str2int(s):
    return DIGITS[s]


def str2float(s):
    index = s.index(".")
    return reduce(lambda x, y: 10 * x + y, map(lambda x: DIGITS[x], s[0: index])) \
           + reduce(lambda x, y: 0.1 * x + y, map(lambda x: DIGITS[x], s[index + 1:].reverse()))


if __name__ == "__main__":
    print(reduce(combine, map(str2int, "1231231")))
    print(reduce(lambda x, y: 10 * x + y, map(lambda x: DIGITS[x], "12321313123")))
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')

    a=101
    print( str(a)==str(a)[::-1])
