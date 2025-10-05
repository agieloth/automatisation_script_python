import pandas as pd
import os
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

from config import GOOGLE_ADS_CREDENTIALS_PATH

def extract_google_ads_data():
    try:

        # Charger les credentials
        client = GoogleAdsClient.load_from_storage(GOOGLE_ADS_CREDENTIALS_PATH)

        # Récupérer le service
        ga_service = client.get_service("GoogleAdsService")

        # ID du client Google Ads (à configurer selon l'id du compte de chaque client)
        customer_id = "631-397-7649"

        # Requête Google Ads : adapter selon ton besoin réel
        query = """
            SELECT
              campaign.name,
              ad_group.name,
              metrics.impressions,
              metrics.clicks,
              metrics.average_cpc,
              metrics.conversions,
              metrics.conversions_value,
              metrics.conversion_value_per_cost,
              segments.date
            FROM
              ad_group
            WHERE
              segments.date DURING YESTERDAY
            LIMIT 10
        """

        # Exécuter la requête
        response = ga_service.search(customer_id=customer_id, query=query)

        # Parser la réponse dans un DataFrame
        rows = []
        for row in response:
            rows.append({
                "Date": row.segments.date,
                "Campaign": row.campaign.name,
                "Ad Group": row.ad_group.name,
                "Impressions": row.metrics.impressions,
                "Clicks": row.metrics.clicks,
                "Average CPC": row.metrics.average_cpc.micros / 1_000_000 if row.metrics.average_cpc else 0,
                "Conversions": row.metrics.conversions,
                "Conversion Value": row.metrics.conversions_value,
                "ROAS": row.metrics.conversion_value_per_cost
            })

        df = pd.DataFrame(rows)
        return df
    
    except GoogleAdsException as ex:
        print(f"Erreur Google Ads API : {ex}")
        return None
    except Exception as e:
        print(f"Erreur générale : {e}")
        return None