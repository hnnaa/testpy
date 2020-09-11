# coding:utf-8
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [('<h1>Hello, %s!</h1>' % (environ["PATH_INFO"][1:] or "web")).encode("utf-8"), b"<h2>yoyo</h2>"]


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8996, application)
print('Serving HTTP on port 8996...')
# 开始监听HTTP请求:
httpd.serve_forever()
