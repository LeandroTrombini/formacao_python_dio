import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente socket criado com sucesso!")

host = 'localhost'
porta = 5433

mensagem = 'Olá servidor'

try:
    print(f"Cliente: {mensagem}")
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode('utf8')
    print(f"Cliente: {dados}")
finally:
    print(f"Cliente: Feachando a conexão")
    s.close()