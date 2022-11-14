import socket

# config server
attendant = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
attendant.bind(('127.0.0.1', 2323))
attendant.listen(5)

# connection to client
client, addr = attendant.accept()

# loop chat
finished = False
while not finished:
  msg = client.recv(1024).decode('utf-8')
  
  # chat end control
  if msg == 'exit':
    client.send('exit'.encode('utf-8'))
    finished = True
  else:
    print(msg)
    client.send(input('Message: ').encode('utf-8')) # any msg
  
client.close()
attendant.close()