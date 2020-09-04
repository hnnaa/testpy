# coding:utf-8

from ctypes import *

dll = windll.LoadLibrary(r'D:\work\project\JOBS\TXWD\JOBS\Holidays\Holidays.dll')

print(dll)

a = dll.Holidays_Init()
print(type(a))
print(a)
