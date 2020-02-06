import funcoes
import socket
chave = "chavesec"
chaveBinaria = funcoes.convert2Bin(chave)

HOST = '172.16.12.52' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('Para sair use CTRL+X\n')
msg = str(input("Digite alguma mensagem\n"))
# criptografar(chave, chaveBinaria, arquivoBinario):
while(msg != 'sair'):
    msgCroptografada = funcoes.criptografar(chave, chaveBinaria, funcoes.convert2Bin(msg))
    udp.sendto(msgCroptografada.encode('utf-8'), dest)
    msg = input()
    msgCroptografada = funcoes.criptografar(chave, chaveBinaria, funcoes.convert2Bin(msg))
udp.close()
