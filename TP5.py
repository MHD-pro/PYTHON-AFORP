import psutil
import os
import time
import platform

def ascii_bar(percent, length=20):
    filled = int(percent / 100 * length)
    return "[" + "#" * filled + "-" * (length - filled) + f"] {percent:.1f}%"

def display_dashboard(logfile=None):
    try:
        while True:
            # Efface l'écran selon l'OS
            os.system('cls' if platform.system() == 'Windows' else 'clear')

            # CPU
            cpu_percents = psutil.cpu_percent(percpu=True)
            cpu_total = psutil.cpu_percent()
            print("=== Utilisation CPU ===")
            for i, p in enumerate(cpu_percents):
                print(f"  Coeur {i}: {ascii_bar(p)}")
            print(f"  Total : {ascii_bar(cpu_total)}")

            # Température CPU (bonus)
            if hasattr(psutil, "sensors_temperatures"):
                temps = psutil.sensors_temperatures()
                if temps:
                    print("=== Température CPU ===")
                    for name, entries in temps.items():
                        for entry in entries:
                            print(f"  {entry.label or name}: {entry.current}°C")

            # RAM
            mem = psutil.virtual_memory()
            print("\n=== Mémoire RAM ===")
            print(f"  Totale : {mem.total // (1024**2)} Mo")
            print(f"  Utilisée: {mem.used // (1024**2)} Mo")
            print(f"  Libre  : {mem.available // (1024**2)} Mo")
            print(f"  Pourcentage : {ascii_bar(mem.percent)}")

            # Disques
            print("\n=== Disques ===")
            for part in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(part.mountpoint)
                    print(f"  {part.device} ({part.mountpoint}) : {ascii_bar(usage.percent)} "
                          f"{usage.used // (1024**3)}/{usage.total // (1024**3)} Go")
                except PermissionError:
                    continue

            # Réseau global
            net = psutil.net_io_counters()
            print("\n=== Réseau (total) ===")
            print(f"  Envoyés : {net.bytes_sent // (1024**2)} Mo, Reçus : {net.bytes_recv // (1024**2)} Mo")
            print(f"  Paquets envoyés : {net.packets_sent}, reçus : {net.packets_recv}")

            # Réseau par interface
            print("\n=== Réseau par interface ===")
            netifs = psutil.net_io_counters(pernic=True)
            for iface, stats in netifs.items():
                print(f"  {iface}: Envoyés {stats.bytes_sent // 1024} Ko, Reçus {stats.bytes_recv // 1024} Ko")

            # Bonus : log dans un fichier
            if logfile:
                with open(logfile, "a") as f:
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')};CPU:{cpu_total};RAM:{mem.percent};"
                            f"DISK:{','.join(str(psutil.disk_usage(p.mountpoint).percent) for p in psutil.disk_partitions())};"
                            f"NET:{net.bytes_sent},{net.bytes_recv}\n")

            print("\nTapez 'quit' puis Entrée pour quitter.")
            for _ in range(5):
                if os.name == 'nt':
                    import msvcrt
                    if msvcrt.kbhit():
                        if msvcrt.getwch().lower() == 'q':
                            return
                else:
                    import sys, select
                    print("Attente (5s)...", end='\r')
                    i, o, e = select.select([sys.stdin], [], [], 1)
                    if i:
                        if sys.stdin.readline().strip().lower() == 'quit':
                            return
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nArrêt demandé par l'utilisateur.")

if __name__ == "__main__":
    # display_dashboard()  # Sans log
    display_dashboard("system_metrics_log.csv")  # Avec log (bonus)