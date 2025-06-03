import re
from collections import Counter
import matplotlib.pyplot as plt
# 1. Ouvrir le fichier auth.log
with open("auth.log", "r", encoding="utf-8") as f:
    lignes = f.readlines()

# 2. Extraire les lignes contenant "Failed password"
failed_lines = [ligne for ligne in lignes if "Failed password" in ligne]

# 3. Extraire les adresses IP avec une regex
ip_regex = re.compile(r"from (\d+\.\d+\.\d+\.\d+)")
ips = [ip_regex.search(ligne).group(1) for ligne in failed_lines if ip_regex.search(ligne)]

# 4. Compter les occurrences de chaque IP
compteur_ips = Counter(ips)

# 5. Afficher les 5 IPs ayant généré le plus d’échecs
print("Top 5 IPs avec le plus d'échecs SSH :")
for ip, count in compteur_ips.most_common(5):
    print(f"{ip} : {count} échecs")




# Visualisation des 5 IPs les plus actives
top_ips = compteur_ips.most_common(5)
ips_labels = [ip for ip, _ in top_ips]
counts = [count for _, count in top_ips]

plt.bar(ips_labels, counts, color='red')
plt.xlabel("Adresse IP")
plt.ylabel("Nombre d'échecs")
plt.title("Top 5 IPs - Échecs de connexion SSH")
plt.tight_layout()
plt.show()

# Extraire les lignes "Accepted password"
accepted_lines = [ligne for ligne in lignes if "Accepted password" in ligne]
ips_accepted = [ip_regex.search(ligne).group(1) for ligne in accepted_lines if ip_regex.search(ligne)]
compteur_ips_accepted = Counter(ips_accepted)

print("\nTop 5 IPs avec le plus de connexions réussies :")
for ip, count in compteur_ips_accepted.most_common(5):
    print(f"{ip} : {count} réussites")
