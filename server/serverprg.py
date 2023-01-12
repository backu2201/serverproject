import socket
indhu = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
indhu.bind((socket.gethostname(),1348))#0-65535 unique port number
indhu.listen()
while True:
    client,address=indhu.accept()
    print("Connection Established")
    print(address)
    client.send(b"socket Programming")
    # https: // github.com / yeddulasaimadhuri / hcl - project.git


