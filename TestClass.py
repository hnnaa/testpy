# encoding:utf-8
import traceback
from types import MethodType


class Student(object):
    _score = 0

    # 限制属性
    # __slots__ = ("name")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)

    # 构造
    def __init__(self, name):
        self.name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("not int value")
        if value < 0 or value > 100:
            raise ValueError("value must between 0 and 100")
        self._score = value


def set_age(self, age):
    self.age = age


s = Student("lilei")
print(s.name)
print("name=" + getattr(s, "name"))
# 绑定方法
s.set_age = MethodType(set_age, s)
s.set_age(18)
print(s.age)
# 设置属性@property
print(s.score)
try:
    s.score = "s"
except:
    print(traceback.format_exc())
try:
    s.score = 1000
except:
    print(traceback.format_exc())
s.score = 100
print(s.score)
try:
    with Student("cc") as ss:
        a = 0
        # ss.name + str((1 / a))
    print("{0:2X},{1:.2f},{2}".format(11, 2.456, 3))
except:
    print(traceback.format_exc())
