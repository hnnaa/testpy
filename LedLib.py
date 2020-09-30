# coding=utf-8
import binascii
import socket
import threading

CARCODE_LED_TYPE = "s"

BUF_SIZE = 1024  # 接收缓冲区
ORDER_ID = 1
lock = threading.Lock()


def get_order_id():
    global ORDER_ID
    with lock:
        ORDER_ID += 1
        if ORDER_ID > 0xFFFF:
            ORDER_ID = 1
        r = ORDER_ID
        return r


def send_rf_led(ip, port, device_type, station, command, data):
    if not ip:
        return 2
    data_len = 0
    length_temp = 18
    if data:
        data_len = len(data)
    length_temp += data_len
    # 更新长度部分
    length = length_temp + 2  # 补上末尾crc的2字节长度
    send_buffer = bytearray(length)
    # 协议头
    send_buffer[0] = 0x01  # 协议版本号 01
    send_buffer[1] = (length >> 8) & 0xFF
    send_buffer[2] = length & 0xFF
    send_order = get_order_id()  # 00 01
    send_buffer[3] = (send_order >> 8) & 0xFF  # 顺序号高字节
    send_buffer[4] = send_order & 0xFF  # 顺序号低字节
    send_buffer[5] = 0x01  # 明文请求
    send_buffer[6] = 0x50  # 源类型
    send_buffer[7] = 0x00  # 源id
    send_buffer[8] = 0x01
    send_buffer[9] = device_type  # 目标类型
    send_buffer[10] = (station >> 8) & 0xFF  # 目标ID
    send_buffer[11] = station & 0xFF
    # 数据部分
    send_buffer[12] = 0x41  # (byte)'R'#  0x41
    send_buffer[13] = 0x42  # (byte)'F'#  0x42
    send_buffer[14] = 0x43  # (byte)'H'#  0x43
    send_buffer[15] = 0x44  # (byte)'Z'#  0x44
    send_buffer[16] = command
    send_buffer[17] = data_len
    if data:
        send_buffer[18:length_temp] = data
    crc = cal_crc16(send_buffer, length_temp)
    send_buffer[-2] = (crc >> 8) & 0xFF
    send_buffer[-1] = crc & 0xFF
    print ("发送led,ip=%s,data=%s"%(ip,binascii.b2a_hex(send_buffer)))
    socket_main = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_main.settimeout(0.5)
    try:
        socket_main.connect((ip, port))
        socket_main.send(send_buffer)
        recv_data = socket_main.recv(BUF_SIZE)
    finally:
        socket_main.close()
    if recv_data and len(recv_data) > 18:
        return recv_data[18]
    return 3


def led_set_customize(ip, port, device_type, station, index, color, display_list, text):
    """

    @param ip:
    @param port:
    @param device_type: 类型
    @param station: 终端编号
    @param index: 发送序号（0:节目打断所有显示，5:节目（现用作余位））
    @param color: 颜色（0x20:绿色）
    @param display_list: 显示效果3个一组（序号（1）+显示时长(2)）最多8组,如：010000 02FFFF,具体参考工具GBK Load.exe
    @param text: 显示内容
    @return:
    """
    if CARCODE_LED_TYPE != device_type:
        return -2
    if not display_list or len(display_list) <= 0 or len(display_list) > 8:
        raise ValueError
    if isinstance(text, unicode):
        text = text.encode("utf-8")
    display_list_str = reduce(lambda x, y: x + y, display_list)
    data = str(index) + str(color) + str(len(display_list_str)) + display_list_str + str(len(text)) + text
    return send_rf_led(ip, port, device_type, station, "\xA5", data)


def led_set_yuwei(ip, port, station, number):
    if number > 9999:
        display_list = ["\x01\x00\x00", "\x07\xFF\xFF", "\x07\xFF\xFF", "\x07\xFF\xFF", "\x07\xFF\xFF", "\x07\xFF\xFF",
                        "\x07\xFF\xFF", "\x07\xFF\xFF"]
        text = "余位" + str(number)
    else:
        display_list = ["\x01\x00\x00", "\x02\xFF\xFF", "\x02\xFF\xFF", "\x02\xFF\xFF", "\x02\xFF\xFF", "\x02\xFF\xFF",
                        "\x02\xFF\xFF", "\x02\xFF\xFF"]
        text = "余位" + "%04d" % number
    return led_set_customize(ip, port, CARCODE_LED_TYPE, station, 5, "\x20", display_list, text)


def cal_crc16(ptr, length):
    crc = 0
    for j in range(length):
        for k in range(8):
            if crc & 0x8000:
                crc *= 2
                crc ^= 0x1021
            else:
                crc *= 2
            if ptr[j] & (0x80 >> k):
                crc ^= 0x1021
        crc &= 0xFFFF
    return crc


if __name__ == "__main__":
    led_set_yuwei("192.167.10.33", 6500, 100, 666)
