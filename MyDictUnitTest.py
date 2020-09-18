# coding:utf-8
import unittest
from MyDict import MyDict


class MyDictUnitTest(unittest.TestCase):
    # 测试项执行前动作
    def setUp(self):
        print("set up!")

    # 测试项结束后动作
    def tearDown(self):
        print("tear down!")

    def test_init(self):
        md = MyDict(a=1, b="bbb")
        self.assertEqual(md.a, 1)
        self.assertEqual(md.b, "bbb")
        self.assertTrue(isinstance(md, dict))

    def test_error(self):
        md = MyDict()
        with self.assertRaises(AttributeError):  # 测试是否引发异常的断言语法
            v = md.empty


if __name__ == "__main__":
    unittest.main()
