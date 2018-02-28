import socket
import time
  
address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
  
while True:  
    msg = time.time()
    if not msg:  
        break
    s.connect(address)
    s.send(str(msg).encode())

s.close()
