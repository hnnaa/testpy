# coding=utf-8
import os
import zipfile
import win32api
import hashlib
import shutil


def get_file_version(file_name):
    info = win32api.GetFileVersionInfo(file_name, os.sep)
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    version = '%d.%d.%d.%d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
    return version


def zip_all(src_dir, dst):
    f = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(src_dir):
        zip_path = root.replace(src_dir, '')
        for filename in files:
            f.write(os.path.join(root, filename), os.path.join(zip_path, filename))
    f.close()
    return os.path.exists(dst)


def get_file_md5(file_name):
    """
    计算文件的md5
    :param file_name:
    :return:
    """
    m = hashlib.md5()  # 创建md5对象
    with open(file_name, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)  # 更新md5对象

    return m.hexdigest()  # 返回md5对象


pathname = r".\bin\Debug"
update_file_dir = r".\bin\update_file"
update_final_dir = r".\bin\update"
target = os.path.join(update_file_dir, "UsbKey.zip")
release = os.path.join(update_file_dir, "release.txt")
ver = get_file_version(os.path.join(pathname, "UsbKeyWindowsService.exe"))
target_final = os.path.join(update_final_dir, "usbkeyapp-%s.zip" % ver)

if os.path.exists(update_file_dir):
    shutil.rmtree(update_file_dir)
if os.path.exists(update_file_dir):
    exit(1)
else:
    os.mkdir(update_file_dir)

if not os.path.exists(update_final_dir):
    os.mkdir(update_final_dir)

# 压缩UsbKey.zip
if not zip_all(pathname, target):
    exit(1)
# 计算MD5
file_md5 = get_file_md5(target)
# 生成release.txt
with open(release, 'wb+') as f:
    con = "ver=" + ver + os.linesep + "url=" + os.linesep + "md5=" + file_md5
    f.write(con.encode())
# 压缩usbkeyapp
if not zip_all(update_file_dir, target_final):
    exit(1)
# 结束
exit()
