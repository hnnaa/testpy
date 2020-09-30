# coding:utf-8

import socket
import sys
import threading
import time
from multiprocessing import Process

DATA_LEN = 1024 * 1024 * 100
IP = "192.168.10.43"


def tcp_link(conn, addr):
    print("server receive:" + addr[0] + ":" + str(addr[1]))
    while True:
        data = conn.recv(DATA_LEN)
        if not data or data.decode() == "exit":
            break
        print("server recv:%s" % data.decode())
        conn.send(b"hello " + data)
        # time.sleep(1)


def new_tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, 6675))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=tcp_link, args=(conn, addr))
        t.setDaemon(True)
        t.start()


def new_tcp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, 6675))
    while True:
        s.send(bytearray(DATA_LEN))
        s.recv(DATA_LEN)
    # for name in ["ad", "abc", "mac"]:
    #     s.send(name.encode())
    #     print(s.recv(1024).decode())

    s.send(b"exit")
    s.close()


if __name__ == "__main__":
    # Process(target=new_tcp_server).start()
    # new_tcp_client()

    # if len(sys.argv) > 1:
    #     if sys.argv[1] == 0:
    #         new_tcp_server()
    # new_tcp_client()
    new_tcp_server()
