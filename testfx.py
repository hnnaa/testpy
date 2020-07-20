# coding:utf-8

# reduce() and map()
import base64
import binascii
import functools
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


def log(text):
    def decorator(func):
        @functools.wraps(func)  # 修改装饰过的函数__name__
        def func_wrapper(*args, **kw):
            if isinstance(text, str):
                print(text)
            print("call:" + func.__name__)
            return func(*args)

        return func_wrapper

    if isinstance(text, str):
        return decorator
    else:
        return decorator(text)


def zs(a, b):
    def func_wrapper(func):
        print("func name=" + func.__name__)
        global buf
        buf[a + "_" + b] = func
        return func

    return func_wrapper


@log("mysum")
def sum_all(*args):
    return reduce(lambda x, y: x + y, args)


def parti_func(a, b, c, d):
    return reduce(lambda x, y: x + y, [a, b, c, d])


def str_to_hex(s):
    return ' '.join([hex(ord(c)).replace('0x', '') for c in s])


def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])


def str_to_bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def bin_to_str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


print("testfx name=" + __name__)
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
    print(sum_all(0.1, 0.2, 0.3))
    print(sum_all.__name__)
    # 偏函数functools.partial
    int2 = functools.partial(int, base=2)
    print("int2:%s" % (int2("10100101")))

    out_source = base64.b64decode(
        "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxLm9XmToNiSMrkHkWhba6MiWzU5JE2OP0K1e72rB/VPYxhqX+IiDI9ZDDr8PpswIu/XyadzfoijfsCBc5KlLvPCjhL5270Ed7DkX6poSYLQhrm6exu8mM579sjnuxjsun3bdppj+zbws0aKdP/Xjqi/PmKLs8GTWv2h6pYj4RM9qKHhPlduczt7RAnd7x/WUYlghwsneQHz3vGVnwZ6mFD91f+hswdyslJgnw9Z9SC69OuIXDupJtMBGSGGX3lBy1v9TTbqJpOalhmfR36zzHrP5fGTHnmHI36ZAdswsVYVaIu41NKZQ+x7w5ejq4Gs3+TEVTOe76ITRwyUt4ocD2QIDAQAB")
    outa = ",".join([str(b) for b in out_source])
    outc = " ".join(['{:02X}'.format(c) for c in out_source])

    print(type(out_source))
