import funcoes
import socket

chave = "chavesec"
chaveBinaria = funcoes.convert2Bin(chave)

host='172.16.12.52'    # Endereco IP do Servidor
port=5000            # Porta que o Servidor esta
udp= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig= (host, port)
udp.bind(orig)
while(1):
    msg, cliente = udp.recvfrom(1024)
    #print (cliente,"mensagem:", msg.decode('ascii'))
    msgDecriptada = funcoes.decriptografar(msg.decode('ascii'), chaveBinaria)
    print (cliente, msgDecriptada)
udp.close()