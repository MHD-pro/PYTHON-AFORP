
"""
Utilisation simple :
python TP3.py --ip 192.168.1.1 --start-port 20 --end-port 1024

Pour le mode multithreadé rapide :
python TP3.py --ip 192.168.1.1 --start-port 20 --end-port 1024 --threads 50

Pour voir les ports fermés :
python TP3.py --ip 192.168.1.1 --start-port 20 --end-port 1024 --verbose

Pour sauvegarder le résultat :
python TP3.py --ip 192.168.1.1 --start-port 20 --end-port 1024 --output resultats.csv"""



import socket
import argparse
import threading
import csv

def scan_port(ip, port, timeout, verbose, results):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        results.append(port)
        print(f"Port {port} ouvert")
    except (socket.timeout, ConnectionRefusedError):
        if verbose:
            print(f"Port {port} fermé")
    except Exception as e:
        if verbose:
            print(f"Erreur sur le port {port}: {e}")
    finally:
        s.close()

def main():
    parser = argparse.ArgumentParser(description="Mini-scanner de ports TCP")
    parser.add_argument('--ip', required=True, help='Adresse IP à scanner')
    parser.add_argument('--start-port', type=int, required=True, help='Premier port à scanner')
    parser.add_argument('--end-port', type=int, required=True, help='Dernier port à scanner')
    parser.add_argument('--timeout', type=float, default=0.5, help='Timeout en secondes (défaut: 0.5)')
    parser.add_argument('--threads', type=int, default=1, help='Nombre de threads (défaut: 1)')
    parser.add_argument('--verbose', action='store_true', help='Afficher aussi les ports fermés')
    parser.add_argument('--output', help='Fichier de sortie (txt ou csv)')
    args = parser.parse_args()

    open_ports = []
    threads = []
    try:
        for port in range(args.start_port, args.end_port + 1):
            t = threading.Thread(target=scan_port, args=(args.ip, port, args.timeout, args.verbose, open_ports))
            threads.append(t)
            t.start()
            if len(threads) >= args.threads:
                for th in threads:
                    th.join()
                threads = []
        # Join remaining threads
        for th in threads:
            th.join()
    except socket.gaierror:
        print("Erreur : Adresse IP invalide.")
        return

    print("\nPorts ouverts :", open_ports)
    if args.output:
        if args.output.endswith('.csv'):
            with open(args.output, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Port'])
                for port in open_ports:
                    writer.writerow([port])
        else:
            with open(args.output, 'w') as f:
                for port in open_ports:
                    f.write(f"{port}\n")
        print(f"Résultats sauvegardés dans {args.output}")

if __name__ == "__main__":
    main()