# coding:utf-8
import traceback
from types import MethodType
from collections.abc import Iterable
from enum import Enum, unique
import testzhuangshiqi

import testfx


class Person(object):
    def __init__(self, name):
        self.name = name


class Student(Person):
    _score = 0
    grade = 1
    i = 0
    kemu = ['a', 'b', 'c']

    # 限制属性
    # __slots__ = ("name")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)

    # 构造
    def __init__(self, name):
        super(Student, self).__init__(name)

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

    # 用户显示
    def __str__(self):
        return "student name=%s" % self.name

    # 开发者显示与用户显示相等
    __repr__ = __str__

    # 可迭代
    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self.kemu):
            raise StopIteration
        item = self.kemu[self.i]
        self.i += 1
        return item

    # 下标获取对象 切片 slice
    def __getitem__(self, item):
        if item >= len(self.kemu) or item + len(self.kemu) < 0:
            raise OverflowError
        return self.kemu[item]

    # 获取未定义属性、方法 (可以作为链式传值) return Student(xxx)
    def __getattr__(self, item):
        if "ws" == item:
            return 99
        if "add" == item:
            return lambda x, y: x + y

    # Callable
    def __call__(self, *args, **kwargs):
        return "my name is {0}".format(self.name)


# __getattr__()链式结构
class Chain(object):
    _path = ''

    def __init__(self, path=''):
        self._path = path

    def __str__(self):
        return self._path

    def __getattr__(self, item):
        if "users" == item:
            return lambda x: Chain('%s/%s/%s' % (self._path, item, x))
        return Chain(('%s/%s' % (self._path, item)))


class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaClass):
    pass


def set_age(self, age):
    self.age = age


# 检查唯一
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def fn(self):
    print('hello world')


# 元类实现ORM
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return 'name=%s;column_type=%s' % (self.name, self.column_type)


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class ModelMetaClass(type):
    def __new__(cls, name, bases, attr):
        print("call ModelMetaClass" + name)
        if 'Model' == name:
            return type.__new__(cls, name, bases, attr)
        mapping = {}
        for k, v in attr.items():
            if isinstance(v, Field):
                mapping[k] = v
        for k in mapping.keys():
            attr.pop(k)
        attr['__mappings__'] = mapping
        attr['__table__'] = name
        return type.__new__(cls, name, bases, attr)


class Model(dict, metaclass=ModelMetaClass):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = "insert into %s (%s) values (%s)" % (self.__table__, ','.join(fields), ','.join(params))
        print('sql=' + sql)
        print('args:' + str(args))


class User(Model):
    id = IntegerField('uid')
    name = StringField('uname')


class InsClass(object):
    name = 's'

    def __getattr__(self, item):
        if item == 'name':
            return 'b'

    def set_stu(self, stu: Student):
        self.stu = stu


# 类属性、实例属性
ic = InsClass()
print('brfore:' + str(ic.__dict__))
ic.name = '1'
print('after:' + str(ic.__dict__))
print(ic.name)
s = Student("lilei")
s1 = Student("laowang")
print(s.name)
print("name=" + getattr(s, "name"))
# 绑定方法
s.set_age = MethodType(set_age, s)
s.set_age(18)
print(s.age)
# 设置属性@property
s.grade = 11
print("s.grade=%d" % s.grade)
print("s1.grade=%d" % s1.grade)
# 显示__str__
print(s)
# 迭代 __iter__
print(isinstance(s, Iterable))
for km in s:
    print("km=" + km)

print("s[0]=%s" % s[0])

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
print("s.add(1,2)=%d" % s.add(1, 2))
print("callbale=" + str(callable(s)), s())

test_chain = Chain().users('jack').status.okl
print("test_chain=", test_chain)

# 枚举
Week = Enum("Week", ("Mon", "Tue"))
for name, member in Week.__members__.items():
    print(name, '=>', member, ',', member.value)

# 元类
Student2 = type('Student2', (object,), dict(hello=fn))
s2 = Student2()
s2.hello()
# metaclass
myList = MyList()
myList.add("b")

ur = User(id=3, name='zmq')
ur.save()

# ORM展现元类
print("end")
