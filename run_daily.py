# FICHIER QUI EXECUTE LE SCRIPT POUR INJECTER LES DONNEES CHAQUE JOUR A 09h00 DU MATIN

import schedule
import time
import subprocess

from datetime import datetime

def job():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Exécution du script main.py...")
    subprocess.run(["python", "main.py"])

# Planification à 09h00
schedule.every().day.at("09:00").do(job)

# Exécuter le script chaque minute
# schedule.every(1).minutes.do(job)


print("Script planificateur lancé. En attente de 09h00 chaque jour...")

while True:
    schedule.run_pending()
    time.sleep(60)