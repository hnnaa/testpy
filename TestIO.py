# encoding:utf-8
import gzip
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

# gzip
uncompressed_data = "yoyoyo,n sdgvfdvdkl司法解释的规定发士大夫感到dsadsfdskfjdkfvbdfdddddddsfdfdvgdff大概的发表反对赌东道赌东道赌东道赌东道\
大师傅但是v地方v豆瓣电饭煲电饭煲大哥v的发表v法担保法大部分的贝多芬发DVD发布电饭煲电饭煲电饭煲bdfbdfbdfadasfdgdffffffffffffffffffffffffffffffs\
大师傅但是v地方v豆瓣电饭煲电饭煲大哥v的发表v法担保法大部分的贝多芬发DVD发布电饭煲电饭煲电饭煲bdfbdfbdfadasfdgdffffffffffffffffffffffffffffffs\
大师傅但是v地方v豆瓣电饭煲电饭煲大哥v的发表v法担保法大部分的贝多芬发DVD发布电饭煲电饭煲电饭煲bdfbdfbdfadasfdgdffffffffffffffffffffffffffffffs\
大师傅但是v地方v豆瓣电饭煲电饭煲大哥v的发表v法担保法大部分的贝多芬发DVD发布电饭煲电饭煲电饭煲bdfbdfbdfadasfdgdffffffffffffffffffffffffffffffs\
大师傅但是v地方v豆瓣电饭煲电饭煲大哥v的发表v法担保法大部分的贝多芬发DVD发布电饭煲电饭煲电饭煲bdfbdfbdfadasfdgdffffffffffffffffffffffffffffffs\
fbbbbbbbbbbbbbbbbbbadsadassssssssssdfsd"
bt_uncompressed_data = uncompressed_data.encode("utf-8")
print("uncompressed_data bt_len=%d,=%s" % (len(bt_uncompressed_data), uncompressed_data))
compressed_data = gzip.compress(bt_uncompressed_data)
print("compressed_data len=%d,=%s" % (len(compressed_data), compressed_data))
de_data = gzip.decompress(compressed_data)
print("de_data=%s" % de_data.decode("utf-8"))
