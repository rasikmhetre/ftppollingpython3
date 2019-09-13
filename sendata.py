import socket
import yaml
import sys
import time
from ftp.py import ftpconn
stream = open('variables.yaml', 'r')
data = yaml.safe_load(stream)
HOST = data["host"]
PORT = data["port"]

s = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("[+] Connected with Server")
file = open(obj,"r")
for i in file.readlines():
  s.send(i.encode())
  time.sleep(0.5)
  
s.close()
