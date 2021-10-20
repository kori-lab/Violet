import os, subprocess;
from requests import get;

def run(functions: dict) -> None:
		
		print("aguarde... pode demorar alguns segundos")
		message = ""
		output = str(subprocess.getstatusoutput('arp -a' if os.name == 'nt' else 'arp')).replace("?", "").replace("(", "").replace(")", "").replace("at", "").replace("\\t", "").replace("\\r", "").replace("ether", "").replace("wlan0", "").replace("din\\x83mico", "").replace("est\\xa0tico", "").split("\\n")
		
		if not output[0][2].replace(" ", "").isdigit():
			output.pop(0)
		if not output[1][2].replace(" ", "").isdigit():
			output.pop(1)
		if not output[2][2].replace(" ", "").isdigit():
			output.pop(2)

		box = []
		for i, v in enumerate(output):
			ip = ""
			ip_check = False
			mac = ""
			mac_check = False
			for letter in v:
				if letter != " ":
					if not ip_check:
						ip += letter

					elif not mac_check: 
						mac += letter

				else:
					if ip: ip_check = True
					if mac: mac_check = True

			box.append({
				"ip": ip.replace(" ", ""),
				"mac": mac.replace("dinƒmico", "").replace("')", "").replace(" ", "")
			})

		for item in box:
			if item['ip'][0].isdigit():
				
				message += functions['colorize'](f"\n\n:blue:Ip::: {item['ip']}\n:blue:Mac::: {item['mac']}\n:green:Api::: \n")
				try:
					# https://macvendors.co/api/{item['mac']}/json
					# https://api.macaddress.io/v1?apiKey=at_pfEl13757ki8H5YM1VPaW9cV7sLyf&output=json&search={item['mac']}

					res = get(f"https://macvendors.co/api/{item['mac']}/json").json()
					for resItem in res:
						if type(res[resItem]) == dict:
							message += functions['colorize'](f" ∟ :c:{resItem}::\n")
							for a in res[resItem]:
									if res[resItem][a]:
										if resItem == "error":
											try:
												resO = get("https://macvendors.co/api/{item['mac']}/json").json()
												print(resO)
												for resItemZ in resO:
													if type(res[resItemZ]) == dict:
														message += functions['colorize'](f" ∟ :c:{resItemZ}::")
														for ab in res[resItemZ]:
																if resO[resItemZ][ab]:
																		message +=  functions['colorize'](f"  :c:{ab}::: {resO[resItemZ][ab]}\n")
													else: 
														message += functions['colorize'](f" ∟ :bg:{resItemZ}::: {resO[resItemZ]}\n")
											except:
												pass;

										else:
											message +=  functions['colorize'](f"  :c:{a}::: {res[resItem][a]}\n")
						else: 
							message += functions['colorize'](f" ∟ :bg:{resItem}::: {res[resItem]}\n")

				except:
						pass;

		exit = False;
		while not exit:
				functions['clear']();

				try:
						message += functions['colorize'](f"\n:c:[+]:: achei mais de :m:{len(box)}:: conexões na rede conectada\n")
						print(message);
						
				except:
						return;

				functions['selfInput']('Aperte enter para ir ao menu...\n');
				
				functions['clear']();
				exit = True;