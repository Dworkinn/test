import socket
import threading

def client_function(socket, sock_ip):
   print("New client connected!", sock_ip)
   
   AlicePublicValue = socket.recv(4096)
   print("Server get Alice public number: ", AlicePublicValue)
   socket.send(str(sock_ip).encode('utf8'))
   
   AlicePublicValue2 = socket.recv(4096)
   print("Server get Alice public number 2: ", AlicePublicValue2)
   socket.close()


   
sock = socket.socket()
sock.bind(("0.0.0.0", 8080))
sock.listen(50)
print("Wait clients...")
while True:
  (socket_ap, addr) = sock.accept()
  client_thread = threading.Thread(target=client_function, args=(socket_ap, addr))
  client_thread.start()
  del(socket_ap)
  del(addr)

if __name__ == "__main__":
    main()
