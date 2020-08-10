# coding:utf-8
import base64
import re
from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
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
