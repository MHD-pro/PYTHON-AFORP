import pandas as pd
import matplotlib.pyplot as plt

def analyze_top_ips(df, top=5):
    counts = df['ip'].value_counts().head(top)
    return counts

def visualize_top_ips(counts):
    plt.figure(figsize=(8,5))
    counts.plot(kind='bar', color='coral')
    plt.title("Top IPs générant le plus d'erreurs 404")
    plt.xlabel("IP")
    plt.ylabel("Nombre d'erreurs 404")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def detect_bots(df):
    bot_keywords = ['bot', 'crawler', 'spider', 'scan', 'curl']
    df['is_bot'] = df['user_agent'].str.lower().apply(lambda ua: any(k in ua for k in bot_keywords))
    return df[df['is_bot']]

def export_results(df_counts, filename_base="resultats"):
    csv_file = f"{filename_base}.csv"
    df_counts.to_csv(csv_file, index=True)
    print(f"Résultats exportés en {csv_file}")

