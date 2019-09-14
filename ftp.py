#!/usr/bin/python3
import os
import time
import ftplib
import yaml
import socket
import sys
import socket
import logging
#time=str(os.system("date +%Y%m%d%H%M%S"))
stream = open('variables.yaml', 'r')
data = yaml.safe_load(stream)
#print (data)
ftplogging=data['loggingfile']
user = data['user']
passwd = data['passwd']
host = data['host']
PORT = data["port"]
#latest_time=None
#latest_name=None
filelocation = data["filelocation"]
logging.basicConfig(filename=ftplogging,level=logging.DEBUG)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
  s.connect((host, PORT))
  class Connector:
###Downloading new file from ftp if found
    def ftpconn(self):
      while True:
        #listing=[]
        ftp = ftplib.FTP(host)
        ftp.login(user=user,passwd=passwd)
        ftp.cwd(filelocation)
        #ftp.retrlines("LIST", listing.append)
        #listing.append(ftp.nlst())
        #print (len(ftp.nlst()))
        for i in range(0,len(ftp.nlst())):
          f = ftp.nlst()[i]
          #print (f)
          obj = open("file.log","r+")
          content = obj.read()
          time=ftp.voidcmd("MDTM "+ftp.nlst()[i])
          if ftp.nlst()[i] in content:
            logging.info("file has already been downloaded")
            pass
          else:
            logging.info("Downloading file",ftp.nlst()[i])
            with open(ftp.nlst()[i],'wb') as file:
              ftp.retrbinary('RETR %s' %f ,file.write)
              logging.info("Download completed")
              #ftp.quit()
              logging.debug('New file has been updated in FTP directory, downloading it...')
              logging.info('New file has been updated in FTP directory, downloading it....')
###Sending data through socket on 514 port
              obj.write(ftp.nlst()[i]+'\n')
              logging.info("[+] Connected with Server")
              obj2=open(ftp.nlst()[i],"r")
              for k in obj2.readlines():
                print (k)
                #s.send(str(k.encode('ascii')))
                s.send(k.encode('utf8'))
                time.sleep(0.5)
              logging.info("Sent logs to DNIF!")
              obj.close()
              os.remove(ftp.nlst()[i])
      s.close()
  con=Connector()
  con.ftpconn()
except ConnectionRefusedError:
  print ("Your DNIF is not listening on 514 port")
  exit(0)
#########################################################
#
#  def sendata(self):
#    s = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
#    s.connect((host, PORT))
#    print("[+] Connected with Server")
#    file = open("logs","r")
#    for i in file.readlines():
#      s.send(i.encode())
#      time.sleep(0.5)
#    s.close()
