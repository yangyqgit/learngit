import socket

def start_client():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('127.0.0.1',9998))
	print(s.recv(1024).decode('utf-8'))
	for data in [b'Michael',b'Tracy',b'Sarah']:
		s.send(data)
		print(s.recv(1024).decode('utf-8'))
	s.send(b'exit')
	s.close()

if __name__=='__main__':
	start_client()
