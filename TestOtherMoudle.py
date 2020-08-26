# coding:utf-8
import os
import random

from PIL import Image, ImageFilter, ImageDraw, ImageFont

print("pillow...")  # 图像处理
# 打开一个jpg图像文件，注意是当前路径:
im_path = r'I:\服务端图片\Capture_Images\20191120\浙K666F1'
file_name = '浙K666F1_20191120141546516.jpg'
im = Image.open(os.path.join(im_path, file_name))
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
# im.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 糊化
im2 = im.filter(ImageFilter.BLUR)
# 把缩放后的图像用jpeg格式保存:
im2.save(os.path.join(im_path, 'thumbnail.jpg'), 'jpeg')


# ImageDraw 生成验证码图片
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

# requests
import requests

r = requests.get("https://baidu.com")
print(r.status_code, r.reason)
print(r.text)
r2 = requests.post("http://saastest.parking24.cn/propConfigcenter/prop/fetch.do", json={
    "series_no": "52425430000000000000012190727005",
    "encode": "false"
})
print(r2.text)
print(r2.json())
print(r2.content)
# 上传文件
# up_f = {"file": open("code.jpg", "rb")}
# r_file = requests.post("http://saastest.parking24.cn/propConfigcenter/prop/fetch.do", files=up_f)
# r.cookies  get(url,timeout=?)

# chardet 检测编码
import chardet

print("chardet...")
d_a = b"hello world"
print(d_a, chardet.detect(d_a))
d_b = "哟哟和v反对"
print(d_b, chardet.detect(d_b.encode('gbk')))
d_c = '最新の主要ニュース'
print(d_c, chardet.detect(d_c.encode('euc-jp')))

# psutil 运维
import psutil

print("psutil...")
print(psutil.cpu_count())  # CPU逻辑数量
print(psutil.cpu_count(logical=False))  # CPU物理核心
print(psutil.cpu_times())  # 统计CPU的用户／系统／空闲时间：
print(psutil.pids())  # 所有进程ID
print(psutil.test())