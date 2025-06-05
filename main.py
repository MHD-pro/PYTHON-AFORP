from log_parser import load_and_parse_log
from data_analyzer import analyze_top_ips, visualize_top_ips, detect_bots, export_results
from network_scanner import scan_ports

def menu():
    filename = "access.log"
    df = None
    df_404 = None
    top_ips = None
    bots_df = None

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Charger et parser le fichier log")
        print("2. Afficher top IPs générant des erreurs 404")
        print("3. Visualiser top IPs erreurs 404")
        print("4. Exporter résultats top IPs")
        print("5. Détecter les bots dans les erreurs 404")
        print("6. Scanner ports d'une IP suspecte")
        print("7. Quitter")
        
        choix = input("Choisissez une option (1-7) : ").strip()

        if choix == '1':
            try:
                df = load_and_parse_log(filename)
                df_404 = df[df['status'] == 404]
                print(f"Fichier chargé avec {len(df)} lignes, {len(df_404)} erreurs 404 détectées.")
            except Exception as e:
                print(f"Erreur lors du chargement : {e}")

        elif choix == '2':
            if df_404 is not None:
                top_ips = analyze_top_ips(df_404)
                print("\nTop IPs avec erreurs 404 :")
                print(top_ips)
            else:
                print("Chargez d'abord le fichier (option 1).")

        elif choix == '3':
            if top_ips is not None:
                visualize_top_ips(top_ips)
            else:
                print("Calculez d'abord le top IPs (option 2).")

        elif choix == '4':
            if top_ips is not None:
                export_results(top_ips, "top_ips_404")
            else:
                print("Calculez d'abord le top IPs (option 2).")

        elif choix == '5':
            if df_404 is not None:
                bots_df = detect_bots(df_404)
                print(f"Nombre de requêtes bots détectées : {len(bots_df)}")
                print("Top IPs bots :")
                print(bots_df['ip'].value_counts().head())
            else:
                print("Chargez d'abord le fichier (option 1).")

        elif choix == '6':
            if top_ips is not None and not top_ips.empty:
                ip_to_scan = input("Entrez une IP à scanner (ou appuyez sur Entrée pour prendre la top IP): ").strip()
                if not ip_to_scan:
                    ip_to_scan = top_ips.index[0]
                print(f"Scan de ports sur {ip_to_scan}...")
                open_ports = scan_ports(ip_to_scan, verbose=True)
                if open_ports:
                    print(f"Ports ouverts sur {ip_to_scan} : {open_ports}")
                else:
                    print(f"Aucun port ouvert détecté sur {ip_to_scan}.")
            else:
                print("Calculez d'abord le top IPs (option 2).")

        elif choix == '7':
            print("Au revoir !")
            break
        else:
            print("Option invalide, réessayez.")

if __name__ == "__main__":
    menu()

