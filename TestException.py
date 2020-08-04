# coding:utf-8
import logging

logging.basicConfig(level=logging.INFO)

try:
    a = 0
    b = 1
    c = b / a
except ZeroDivisionError as e:
    print("error=", e)
    # logging记录日志
    logging.exception(e)

# 调试：断言assert抛出异常 用-O可以取消执行中
try:
    a = 0
    b = 1
    assert a != 0, "a is 0"
    c = b / a
except ZeroDivisionError as e:
    print("error=", e)
except AssertionError as ae:
    print("assert error=", ae)

# 调试：logging
logging.info("i am logging")
