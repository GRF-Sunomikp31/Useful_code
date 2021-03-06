'''
通信协议：
    stm32 to Jeston nano：0x5a/0x5a/ring/task/power/0xb3
    Jeston nano to stm32：0x5a/0x5a/mark/result/0xb3
    以上数据均为16进制
'''
import serial
import threading
import time


def receive():
    while True:
        #这里stm32发送信息以什么为结尾？回车吗
        tran_data1 = ord(serial_port.read() )
        if tran_data1 == 90:
            tran_data2 = ord(serial_port.read())
            if tran_data2 == 90:
                ring = ord(serial_port.read())
                task = ord(serial_port.read())
                power = ord(serial_port.read())
                print("data receive success!")

def send(mark,result):
    while True:
        data = bytearray([0x5a, 0x5a, mark,result, 0xb3])
        print(data)
        serial_port.write(data)
        time.sleep(1)

if __name__ == '__main__':
    serial_port = serial.Serial(
        port="COM5",
        baudrate=115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
    )
    # Wait a second to let the port initialize
    time.sleep(0.5)
    mark = 0
    result = 1
    t1 = threading.Thread(target=receive)
    t2 = threading.Thread(target=send,args=[mark,result])
    t1.start()
    t2.start()
    t1.join()
    t2.join()