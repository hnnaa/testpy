# coding:utf-8
import base64
import hashlib
import hmac
import re
import struct
from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone

t = 0


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    m = re.match("(UTC)([-+]{1})(\d+):(\d+)", tz_str)
    if m.group(2) == "+":
        tz = timezone(timedelta(hours=float(m.group(3)), minutes=float(m.group(4))))
    else:
        tz = timezone(-timedelta(hours=float(m.group(3)), minutes=float(m.group(4))))

    return dt.replace(tzinfo=tz).timestamp()


# 1.datetime
print("1.datetime")
now = datetime.now()
print(now)
# 指定时间
dt = datetime(1990, 2, 6, 2, 5)
print(dt)
# timestamp
print(dt.timestamp())
print(datetime.fromtimestamp(dt.timestamp() - 10000))
print(datetime.utcfromtimestamp(dt.timestamp() - 10000))
# 时间戳
cday = datetime.strptime("2019-06-04 05:44:22", "%Y-%m-%d %H:%M:%S")
print(cday)
print(cday.strftime("%a %b %d"))
# timedelta 时间加减
print(cday - timedelta(hours=2))
# 时区
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置时区
print(dt.astimezone(timezone(timedelta(hours=9))))  # 时区转换

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC-7:00')
t2 = to_timestamp('2015-6-1 08:10:30', 'UTC-7:30')
print(t1)
print(t2)

# 2.collections
print("2.collections")
# namedtuple 创建一个自定义的tuple对象,不用index表示tuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)
p2 = Point._make((2, 3))
print(p2.x, p2.y)
# deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(["a", "b", "c"])
q.appendleft("f")
print(q.popleft())
# defaultdict 没有key时返回默认值
dd = defaultdict(lambda: "N/A")
print(dd["key"])
# OrderedDict 有序
d = dict([('a', 1), ('b', 2), ('c', 3), ('aa', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)
print(od)
# ChainMap dict的组合，在输出同一个key时，按优先级输出value 输入参数，环境变量、默认参数的好选择
a1 = {"co": 11}
a2 = {"co": 1, "bo": 2}
a3 = {"co": 1, "bo": 22, "do": 3}
combined = ChainMap({}, a1, a2, a3)
print("co=%s,bo=%s,do=%s" % (combined["co"], combined["bo"], combined["do"]))
# Counter 计数器 计算字符出现的次数
c = Counter()
c.update("lkjfsdfsssds")
print(c)

# 3.base64
print("3.base64")
b1 = base64.b64encode(b'\x11\x34abc')
print(b1)
print(base64.b64decode(b1))
# url 安全
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

# struct 解决byte的转换
print("struct...")
print(struct.pack('>I', 1024009))  # >:大端 I:四字节无符号 H:2字节无符号 c:char
print(struct.unpack('>H', b'\x00\x01'))
print(struct.unpack('>H', b'\x01\x00'))
print(struct.unpack('c', b'\x41'))
print(list(bytearray.fromhex('fbd32456')))

# hashlib 摘要算法  什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
print("hashlib...")
s2 = 'how to use md5 in python hashlib?'
md5 = hashlib.md5()
md5.update(s2.encode('utf-8'))
print("md5=" + md5.hexdigest())
sha1 = hashlib.sha1()
sha1.update(s2.encode("utf-8"))
print("sha1=" + sha1.hexdigest())

# hmac
message = b'hello world'
key = b'se'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print("hmac=" + h.hexdigest())

# itertools 操作迭代对象的函数。
import itertools

natuals = itertools.count(1)  # 创建无限额自然数迭代器
ns = itertools.takewhile(lambda x: x <= 10, natuals)  # takewhile 截断
print(type(ns))
print(list(ns))
cs = itertools.cycle('ABC')  # cycle 无限循环序列 注意字符串也是序列的一种
for c in cs:
    print(c)
    if c == 'C':
        break
ns = itertools.repeat('A', 3)  # repeat 重复一个元素
for c in itertools.chain(['a', 'b'], ['c', 'd']):  # chain 串联迭代对象
    print(c)
for key, group in itertools.groupby('AABBccDADaa', lambda c: c.upper()):  # 将迭代对象中相邻的重复元素挑出来放在一起
    print(key, list(group))


def pi(N):
    odds = itertools.takewhile(lambda x: x <= 2 * N - 1, itertools.count(1, 2))
    return sum(map(lambda x: (-1) ** ((x - 1) / 2) * 4 / x, odds))


print(pi(1000000))

# 只要正确实现了上下文管理，就可以用于with语句 __enter__和__exit__
print("contextlib...")


class Query(object):

    def __init__(self, name):
        self.name = name
        print(name)

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('test with') as f:
    f.query()


# @contextmanager yield(执行with内的代码,也可以加返回)
@contextmanager
def do_tasks():
    print("begin tasks")
    yield
    print("end tasks")


with do_tasks():
    print("do task 1")
    print("do task 2")

# @closing  将没有实现上下文的对象用变为上下问对象
from contextlib import closing


class NoContext:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name + " show")

    def close(self):
        print(self.name + " closed")


with closing(NoContext("NoContext!!")) as f:
    f.show()

# urllib 操作url的功能
print("urllib...")
from urllib import request

with request.urlopen("http://www.baidu.com") as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print(k + ":" + v)

# urlopen() 只需要把参数data以bytes形式传入。
req1 = request.Request("http://saastest.parking24.cn/propConfigcenter/prop/fetch.do",
                       data=b"{\"series_no\":\"52425430000000000000012190727005\",\"encode\":\"false\"}")
req1.add_header("content-type", "application/json")
with request.urlopen(req1) as f2:
    print(f2.read())
# HTMLParser
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
