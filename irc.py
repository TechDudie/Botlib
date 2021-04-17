# Copied and edited from Portal by @TechDudie
import socket
import string
import sys
HOST = "chat.freenode.net"
PORT = 6667
NICK = "Portal"
PASSWORD = os.getenv("PASSWORD")
CHANNEL = "##techdudeserver"
SERVER = ""
readbuffer = ""
send = s.send
s = socket.socket()
s.connect((HOST, PORT))
send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
send(bytes("USER %s %s %s :%s\r\n" % (NICK, NICK, NICK, NICK), "UTF-8"))
send(bytes("JOIN {}\r\n".format(CHANNEL), "UTF-8"))
s.send(bytes("PRIVMSG NickServ :identify {}\r\n".format(PASSWORD), "UTF-8"))
readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
temp = str.split(readbuffer, "\n")
readbuffer = temp.pop()
for line in temp:
    SERVER = str.rstrip(line)[1:].split()[0]
    print(str.rstrip(line))
while 1:
    readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()
    for line in temp:
        print(str.rstrip(line))
        message = str.rstrip(line).split(" PRIVMSG {} :".format(CHANNEL))
        if "PING" in line:
            send("PONG :{}\r\n".format(SERVER).encode("utf-8"))
