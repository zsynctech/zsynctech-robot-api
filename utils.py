import socket

def get_local_ip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        return "Não localizado"

    return local_ip
