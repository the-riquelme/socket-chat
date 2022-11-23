from threading import Thread
import socket

# config server
attendant = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
attendant.bind(('127.0.0.1', 2525))
attendant.listen(5)

print('Starting the chat...')

def acceptUser(client, clientNumber):
  finished = False
  while not finished:
    msg = client.recv(1024).decode('utf-8')

    # chat end control
    if msg == 'exit':
      client.send('exit'.encode('utf-8'))
      finished = True
    else:
      print('Message Thead ' + str(clientNumber) + ': ' + msg)
      client.send(input('Message: ').encode('utf-8')) # any msg

  client.close()

# loop chat
finished = False
count = 1
while not finished:
  # connection to client
  client, addr = attendant.accept()
  Thread(target=acceptUser, args=(client, count)).start()
  count = count + 1

  # chat end control

attendant.close()