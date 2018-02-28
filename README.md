# UDP_Socket
UDP Socket in python
没有TCP那么复杂，三次握手，错误重传, 流量控制之类的机制都没，发的只管发，收得只管收

server端
建立数据报形式的socket
公开一个端口，一边客户端连接
开始接收数据

client端
新建一个数据报socket
收发数据


#Notes
当接收端有延时，比如sleep或者在真实场景中产生的延时，需要setsockopt()将接收缓存(SO_RCVBUF)，（本方法不能从根本解决问题，只能改善）
或采用多线程接包处理
