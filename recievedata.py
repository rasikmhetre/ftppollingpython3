import socket
import sys


HOST = "192.168.86.46"
PORT = 514

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
s.settimeout(172800)
print("Listening ...")

while True:
    conn, addr = s.accept()
    print("[+] Client connected: ", addr)

    # get file name to download
    #f = open("recieved_logfile", "wb")
    while True:
        # get file bytes
        data = conn.recv(4096)
        print (data.decode('utf8'))
        if not data:
            break
        # write bytes on file
   #     f.write(data)
#    f.close()
    print("[+] Download complete!")

    # close connection
#    conn.close()
    print("[-] Client disconnected")
    sys.exit(0)
