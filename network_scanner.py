import socket

def scan_port(ip, port, timeout=1):
    """
    Teste si un port TCP est ouvert sur l'IP donnée.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        result = s.connect_ex((ip, port))
        return result == 0  # True si ouvert

def scan_ports(ip, ports=[22, 80, 443], verbose=False):
    """
    Scanne une liste de ports sur l'IP, affiche résultats si verbose.
    Retourne la liste des ports ouverts.
    """
    open_ports = []
    for port in ports:
        if scan_port(ip, port):
            open_ports.append(port)
            if verbose:
                print(f"[+] {ip}:{port} ouvert")
        else:
            if verbose:
                print(f"[-] {ip}:{port} fermé")
    return open_ports
