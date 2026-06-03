import csv
from django.core.management.base import BaseCommand
from dashboard.models import FarmData
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = "Load farm data from CSV into database"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to CSV file")

    def handle(self, *args, **options):
        path = options["csv_file"]
        self.stdout.write(f"Loading from {path} ...")
        
        # Clear existing data
        FarmData.objects.all().delete()
        self.stdout.write("Cleared existing data.")

        batch = []
        count = 0

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Handle both old and new column names
                hum_key = "relative_humidity_%" if "relative_humidity_%" in row else "relative_humidity"
                moist_key = "soil_moisture_%" if "soil_moisture_%" in row else "soil_moisture"

                batch.append(FarmData(
                    state=row["state"],
                    city=row["city"],
                    crop_type=row["crop_type"],
                    air_temperature_c=float(row["air_temperature_c"]),
                    relative_humidity=float(row[hum_key]),
                    rainfall_mm=float(row["rainfall_mm"]),
                    wind_speed_mps=float(row.get("wind_speed_mps", 0) or 0),
                    solar_radiation_wm2=float(row.get("solar_radiation_wm2", 0) or 0),
                    soil_moisture=float(row[moist_key]),
                    soil_temperature_c=float(row.get("soil_temperature_c", 0) or 0),
                    soil_ph=float(row["soil_ph"]),
                    growth_stage=row.get("growth_stage", ""),
                    crop_health_index=int(float(row["crop_health_index"])),
                    crop_duration_days=int(float(row.get("crop_duration_days", 120) or 120)),
                    irrigation_status=row.get("irrigation_status", "OFF"),
                    fertilizer_applied=row.get("fertilizer_applied", "NONE"),
                    pest_risk_level=row.get("pest_risk_level", "LOW"),
                    region=row["region"],
                    datetime=parse_datetime(row.get("datetime", "") or "") if row.get("datetime") else None,
                ))
                count += 1

                if len(batch) >= 1000:
                    FarmData.objects.bulk_create(batch)
                    batch = []
                    self.stdout.write(f"  Inserted {count} rows...")

        if batch:
            FarmData.objects.bulk_create(batch)

        self.stdout.write(self.style.SUCCESS(f"✅ Done! Loaded {count} rows total."))
