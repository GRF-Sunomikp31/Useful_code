# serial

## 代码分析：

1、**muiltithreading_serial:**自定义通信协议，Python多线程调用serial实现串口同时收发数据。

2、**Multiprocessing_serial：**自定义通信协议，Python**多进程**调用serial实现串口同时收发数据。

​		这里因为使用的是多进程，无法在serial中同时用两个进程（其实是两个CPU）同时调用端口。


