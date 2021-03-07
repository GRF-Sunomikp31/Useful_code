'''
通信协议：
    stm32 to Jeston nano：0x5a/0x5a/ring/task/power/0xb3
    Jeston nano to stm32：0x5a/0x5a/mark/result/0xb3
    以上数据均为16进制
'''
import serial
import multiprocessing
import time

def receive():
    serial_port = serial.Serial(
        port="COM5",
        baudrate=115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
    )
    # Wait a second to let the port initialize
    time.sleep(0.5)
    while True:
        tran_data1 = ord(serial_port.read() )
        if tran_data1 == 90:
            tran_data2 = ord(serial_port.read())
            if tran_data2 == 90:
                ring = ord(serial_port.read())
                task = ord(serial_port.read())
                power = ord(serial_port.read())
                print("data receive success!")

def send(mark,result):
    serial_port = serial.Serial(
        port="COM7",
        baudrate=115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
    )
    # Wait a second to let the port initialize
    time.sleep(0.5)
    while True:
        data = bytearray([0x5a, 0x5a, mark,result, 0xb3])
        print(data)
        serial_port.write(data)
        time.sleep(1)


if __name__ == '__main__':
    mark = 0
    result = 1
    p1 = multiprocessing.Process(target=send,args=[mark,result])
    p2 = multiprocessing.Process(target=receive)
    p1.start()
    p2.start()
    p1.join()
    p2.join()