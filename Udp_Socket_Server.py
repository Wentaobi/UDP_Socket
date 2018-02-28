import socket  
import time

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
s.bind(address)  
  
while True:  
    data, addr = s.recvfrom(2048)  
    if not data:  
        print("client has exist")
        break  
    print("received time:", data, "from", addr)
    print("current time :", time.time())
  
s.close()  
