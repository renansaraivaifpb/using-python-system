# verificar se o localhost está configurando para 127.0.0.1
# verificar se o request foi atendido, caso sim: há internet, caso contrário: não há internet
import socket
import requests

def verificar_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def verificar_conexacao_a_internet():
    request = requests.get("http://www.google.com")
    return request.status_code == 200
