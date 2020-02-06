import funcoes
import socket

chave = "chavesecreta"
chaveBinaria = funcoes.convert2Bin(chave)

host='172.16.12.52'    # Endereco IP do Servidor
port=5000            # Porta que o Servidor esta
udp= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig= (host, port)
udp.bind(orig)
while True:
    msg, cliente = udp.recvfrom(1024)
    msgDecriptada = funcoes.decriptografar(msg, chaveBinaria)
    print (cliente, msg)
udp.close()