import pygsheets
import pandas as pd
import json
import os

from config import GOOGLE_SHEET_NAME


def inject_data_to_sheet(df: pd.DataFrame):
    try:
        # Chargement de la configuration du 
        with open('sheets/sheet_config.json') as f:
            sheet_config = json.load(f)

        spreadsheet_id = sheet_config['spreadsheet_id']
        sheet_name = sheet_config['sheet_name']

        # Pour charger les credentials depuis l’environnement
        gc = authorize_from_env()

        # Authentification avec le fichier de service (service account)
        # gc = pygsheets.authorize(service_file='credentials/google_ads_credentials.json')

        # Ouvrir le google sheet avec son ID
        sh = gc.open_by_key(spreadsheet_id)

        try:
            # Tenter d'ouvrir l'onglet existant
            wks = sh.worksheet_by_title(sheet_name)
        except pygsheets.WorksheetNotFound:
            #Créer l'onglet s'il n'existe pas
            wks = sh.add_worksheet(sheet_name)

        # Ecrire le dataFrame dans le sheet à partir de A1
        wks.clear()
        wks.set_dataframe(df, (1, 1))

        print(f"Données injectées avec succès dans l'onglet '{sheet_name}'.")


    except Exception as e:
        print(f"Erreur lors de l'injection dans Google Sheet : {e}")    


def authorize_from_env():
    json_creds = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not json_creds:
        raise Exception("La variable d'environnement GOOGLE_SERVICE_ACCOUNT_JSON est manquante.")

    creds_dict = json.loads(json_creds)
    gc = pygsheets.authorize(service_account_credentials=creds_dict)
    return gc