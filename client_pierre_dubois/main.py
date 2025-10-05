# from scripts.extract_google_ads import extract_google_ads_data

from scripts.mock_google_ads_data import extract_google_ads_data
from scripts.inject_to_sheets import inject_data_to_sheet

def main() :
    print("Démarrage du script...")

    df = extract_google_ads_data()
    if df is not None:
        inject_data_to_sheet(df)
    else:
        print("Aucune donnée extraite")
    

if __name__ == "__main__":
    main()