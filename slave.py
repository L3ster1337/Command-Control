#L3ster in 1337 '-'
#!/usr/bin/python
import sys
import os
import subprocess 
from subprocess import PIPE, Popen

cmd = sys.argv[2]


if(len(sys.argv) < 2):
	print("Usage: python3 slave.py 127.0.0. 'uname -a' -> deve-se omitir o valor do ultimo bloco")
	sys.exit()

for x in range(242,245):

	var1 = sys.argv[1]
	var2 = str(x)
	
	host =  var1 + var2

	try:

		print('[Info] Attempt on host: ' + host + '\n')
		connect = 'bandit0@' + host
		stream = subprocess.run(['sshpass', '-p', 'bandit0', 'ssh', connect, '-p','2220', cmd], timeout=7)
		

	except subprocess.TimeoutExpired as e:
		print('[!] Connection Timeout for host: ' + host + ' [!]\n')
	
