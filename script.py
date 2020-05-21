# coding:utf-8

import os, os.path, re

android_tool_path = "C:\\Android\\Sdk\\build-tools\\29.0.3\\"


def searchFile(pathname, filename):  # 参数1要搜索的路径，参数2要搜索的文件名，可以是正则表代式
    matchedFile = []
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if re.match(filename, file):
                fname = os.path.abspath(os.path.join(root, file))
                # print(os.path.splitext(os.path.basename(fname))[0])
                matchedFile.append(fname)
    return matchedFile


files = searchFile(r".\\", "scriptplus-v[\\d]+\.[\\d]+\.[\\d]+\.jar")
if files is not None:
    a = files[0]
    b = os.path.join(os.path.dirname(a), os.path.splitext(os.path.basename(a))[0] + "-android" + \
                     os.path.splitext(os.path.basename(a))[1])
    os.system("copy %s %s" % (a, b))
    os.system("%sdx.bat --dex --output=classes.dex %s" % (android_tool_path, b))
    os.system("%saapt.exe add %s classes.dex" % (android_tool_path, b))
    exit()
exit(1)
