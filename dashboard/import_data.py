import pandas as pd

from dashboard.models import FarmData

df = pd.read_csv(
    "dataset/FarmEye_All_India_Combined_Dataset_Shuffled (1).csv"
)

for _, row in df.iterrows():

    FarmData.objects.create(
        state=row["state"],
        city=row["city"],
        crop_type=row["crop_type"],
        air_temperature_c=row["air_temperature_c"],
        relative_humidity=row["relative_humidity_%"],
        rainfall_mm=row["rainfall_mm"],
        soil_moisture=row["soil_moisture_%"],
        soil_ph=row["soil_ph"],
        crop_health_index=row["crop_health_index"],
        region=row["region"]
    )

print("Data Imported Successfully")