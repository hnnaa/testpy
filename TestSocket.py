# coding:utf-8

import socket
import threading
import time
from multiprocessing import Process


def tcp_link(conn, addr):
    print("server receive:" + addr[0] +":"+ str(addr[1]))
    while True:
        data = conn.recv(1024)
        if not data or data.decode() == "exit":
            break
        print("server recv:%s" % data.decode())
        conn.send(b"hello " + data)
        time.sleep(1)


def new_tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 6675))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=tcp_link, args=(conn, addr))
        t.start()


def new_tcp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 6675))
    for name in ["ad", "abc", "mac"]:
        s.send(name.encode())
        print(s.recv(1024).decode())

    s.send(b"exit")
    s.close()


if __name__ == "__main__":
    Process(target=new_tcp_server).start()
    new_tcp_client()
