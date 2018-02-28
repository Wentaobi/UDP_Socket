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
