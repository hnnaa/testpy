# encoding:utf-8
import traceback


class Student(object):
    __slots__ = ["name"]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)

    def __init__(self, name):
        self.name = name


s = Student("fdf")
print(s.name)
# s.ff = ""
try:
    with Student("cc") as ss:
        a = 0
        # ss.name + str((1 / a))
    print("{0:2X},{1:.2f},{2}".format(11, 2.456, 3))
except:
    print(traceback.format_exc())
