import socket

HOST = 'localhost'
PORT = 5000

def run_client(req):
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  HOST = socket.gethostname()

  client.connect((HOST, PORT))


  try:
    client.sendall(req.encode('utf-8'))
    
    res = client.recv(1024).decode('utf-8')

    print('Server says: ' + res)
  finally:
    client.close()
    return res
  

# run_client('uhh')