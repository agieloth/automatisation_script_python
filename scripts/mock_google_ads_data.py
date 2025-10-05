# scripts/mock_google_ads_data.py

import pandas as pd
from datetime import datetime, timedelta

def extract_google_ads_data():
    # Simuler des données pour "hier"
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    data = [
        {
            "Date": yesterday,
            "Campaign": "Campagne Test A",
            "Ad Group": "Ad Group 1",
            "Impressions": 1200,
            "Clicks": 150,
            "Average CPC": 0.45,
            "Conversions": 10,
            "Conversion Value": 150.50,
            "ROAS": 2.5
        },
        {
            "Date": yesterday,
            "Campaign": "Campagne Test B",
            "Ad Group": "Ad Group 2",
            "Impressions": 750,
            "Clicks": 80,
            "Average CPC": 0.65,
            "Conversions": 5,
            "Conversion Value": 90.90,
            "ROAS": 1.9
        }
    ]

    df = pd.DataFrame(data)
    return df
