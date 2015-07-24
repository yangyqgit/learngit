import socket
import threading,time

def tcplink(sock,addr):
	print('Accept new connection from %s:%s'% addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('hello, %s' % data).encode('utf-8'))
	sock.close()
	print('connection from %s:%s closed.'%addr)

def start():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(('127.0.0.1',9998))
	s.listen(5)
	print('waiting for connection...')
	while True:
		sock,addr = s.accept()
		t = threading.Thread(target=tcplink,args=(sock,addr))
		t.start()

if __name__=='__main__':
	start()
