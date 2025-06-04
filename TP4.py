import pandas as pd
import re
import matplotlib.pyplot as plt

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) \S+ "(?:[^"]*)" "(?P<user_agent>[^"]*)"'
)

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        return match.groupdict()
    return None

def load_log_to_df(filepath):
    records = []
    with open(filepath, encoding='utf-8', errors='ignore') as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                records.append(parsed)
    df = pd.DataFrame(records)
    print("Aperçu du DataFrame :")
    print(df.head())
    return df

def filter_404(df):
    df_404 = df[df['status'] == '404']
    print(f"Nombre d'erreurs 404 : {len(df_404)}")
    return df_404

def top5_ips(df_404):
    top_ips = df_404['ip'].value_counts().head(5)
    print("Top 5 IPs générant le plus d'erreurs 404 :")
    print(top_ips)
    return top_ips

def plot_histogram(top_ips):
    plt.figure(figsize=(8,5))
    top_ips.plot(kind='bar', color='tomato')
    plt.title("Top 5 IPs générant des erreurs 404")
    plt.xlabel("Adresse IP")
    plt.ylabel("Nombre d'erreurs 404")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

def detect_bots(df_404):
    bot_regex = re.compile(r'bot|crawler|spider', re.IGNORECASE)
    bots = df_404[df_404['user_agent'].str.contains(bot_regex, na=False)]
    bot_ips = bots['ip'].value_counts()
    percent = 100 * len(bots) / len(df_404) if len(df_404) > 0 else 0
    print(f"\nPourcentage d'erreurs 404 provenant de bots : {percent:.2f}%")
    print("IPs suspectes (bots) :")
    print(bot_ips.head())
    return bots, percent

def main():
    log_path = "access.log"  # À adapter si besoin
    df = load_log_to_df(log_path)
    df_404 = filter_404(df)
    top_ips = top5_ips(df_404)
    plot_histogram(top_ips)
    bots, percent = detect_bots(df_404)

    print("\nDiscussion :")
    print("- Les IPs générant beaucoup d'erreurs 404 peuvent être des scanners ou des bots malveillants.")
    print("- Il peut être pertinent de surveiller ou bannir les IPs les plus actives, surtout si elles sont identifiées comme bots.")
    print("- Ce type de détection peut être automatisé (script régulier, alertes, etc.).")

if __name__ == "__main__":
    main()