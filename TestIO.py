# encoding:utf-8
import json
import pickle
from io import StringIO
from io import BytesIO
import shutil

f = StringIO()
f.write("abc")
print(f.getvalue())
f.close()

f2 = BytesIO()
f2.write(u"中文".encode("utf-8"))
print(f2.getvalue().decode("utf-8"))
f2.close()

# 序列化 pickle
d = dict(a=1, b=2, c=3)
print(pickle.dumps(d))
f = open('test.txt', 'wb')
pickle.dump(d, f)
f.close()
f2 = open('test.txt', 'rb')
c = pickle.load(f2)
f2.close()
print(c)
# json
obj = dict(name="小明", age=18)
s = json.dumps(obj, ensure_ascii=False)
print(s)


# json obj
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


st = json.loads(s, object_hook=lambda d: Student(d['name'], d['age']))
st2str = json.dumps(s, default=lambda s: s.__dict__)
print(st2str)