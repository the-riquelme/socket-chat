import socket

# config and connect client to attendant
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 2323))

finished = False
print('Type exit to end the chat...')

# loop chat
while not finished:
  client.send(input('Message: ').encode('utf-8')) # any msg
  msg = client.recv(1024).decode('utf-8')
  
  # chat end control
  if msg == 'exit':
    finished = True
  else:
    print(msg)
    
client.close()