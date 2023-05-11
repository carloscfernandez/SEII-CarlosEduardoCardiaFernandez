'''O socket tem bastante influencia ao tratar de servidores
com grande quantidade de requisicoes e chamadas'''

# --- Importando os modulos necessarios ---
import socket       # modulo para sockets
import threading    # modulo para threads


HEADER = 64
PORT = 5050                                               #P orta de acesso     
SERVER = socket.gethostbyname(socket.gethostname())       #forma padrao para adquirir o IP do host
ADDR = (SERVER, PORT)                                     # Endereco para realizar o server bind (utilizando o Server IP e a Porta de Acesso)
FORMAT = 'utf-8'                                          # Formato de decodificacao
DISCONNECT_MESSAGE = "!DISCONECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #declarando o servidor
server.bind(ADDR)                                           # utilizando o metodo bind com a Server IP e a Porta de Acesso

# Realiza o controle de conexoes dos clientes
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
          msg_lenght = int(msg_lenght)
          msg = conn.recv(msg_lenght).decode(FORMAT)
          if msg == DISCONNECT_MESSAGE:
              connected = False
            
          print(f"[addr] {msg}")
          conn.send("Msg receveid". encode(FORMAT))
    conn.close()

def start():
    server.listen()                                        # com esse comando o socket 'ouve/escuta' as solicitacoes do client
    print("[LISTENING} Server is listening on {SERVER}")
    while True:                                            # fica travado neste laco
        conn, addr = server.accept()                       # aceita a chamada de um cliente e ao conectar salva a conexao e o endereco do cliente
        thread = threading.Thread(target=handle_client, args=(conn, addr))     # a thread eh utilizada para realizar as acoes solicitadas pelo cliente 
        thread.start()                                                         # inicia a thread 
        print(f"[ACTIVE CONNECTIONS} {threading.activeCount() - '}")

# inicia a funcao start que permanece no laço #while(True)
print("[STARTING] server is starting...")
start()                   
