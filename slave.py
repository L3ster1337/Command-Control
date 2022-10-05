#L3ster in 1337 '-'
#!/usr/bin/python
import sys
import os
import subprocess 
from subprocess import PIPE, Popen

user = sys.argv[2]
password = sys.argv[3]
cmd = sys.argv[4]


if(len(sys.argv) <= 4):
	print("Usage: python3 slave.py 13.50.18. bandit0 bandit0 'id' -> deve-se omitir o valor do ultimo bloco do IP\n python3 slave.py <IP-SEM-FINAL> <User> <Pass> '<Comando>'") #primeiro bandit0 eh o user, o segundo a senha
	sys.exit()

for x in range(242,245): #range proposital para testar o .243, IP do Bandit0, assim como verificar o funcionamento do timeout 

	var1 = sys.argv[1]
	var2 = str(x)
	
	host =  var1 + var2

	try:

		print('[Info] Attempt on host: ' + host + '\n')
		connect = user + '@' + host
		stream = subprocess.run(['sshpass', '-p', password, 'ssh', connect, '-p','2220', cmd], timeout=7) # Timeout setado para 7 segundos
		

	except subprocess.TimeoutExpired as e:
		print('[!] Connection Timeout for host: ' + host + ' [!]\n')
	
