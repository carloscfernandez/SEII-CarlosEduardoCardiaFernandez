'''O socket tem bastante influencia ao tratar de servidores
com grande quantidade de requisicoes e chamadas'''

# --- Importando os modulos necessarios ---

import socket       #modulo para sockets

HEADER = 64
PORT = 5050                                           #porta de acesso
SERVER = socket.gethostbyname(socket.gethostname())   #IP do servidor 
ADDR = (SERVER, PORT)                                 #Address do servidor
FORMAT = 'utf-8'                                      #formato para codificacao
DISCONNECT_MESSAGE = "!DISCONECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #declarando o client
client.connect(ADDR)                                              #atribuindo as características do client (server, PORT)


def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(msg_lenght)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    
send("HELLO WORLD!")
input()
send("HELLO EVERYONE!")
input()
send("HELLO TIM!")

send(DISCONNECT_MESSAGE)
