import socket

HOST = 'localhost'
PORT = 5000

def process_req(req):
  return f'wym "{req}" lol'

def run_server():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  HOST = socket.gethostname()

  server.bind((HOST, PORT))
  server.listen(1)

  try:
    while True:
      print('waiting for connection')
      conn, addr = server.accept()
      print(f"Connection from {addr}")
      data = conn.recv(1024).decode('utf-8')
      
      if data:
        print("Client says: " + data)
        res = process_req(data)
        conn.send(res.encode('utf-8'))
      else:
        break
  finally:
    conn.close()

run_server()
    