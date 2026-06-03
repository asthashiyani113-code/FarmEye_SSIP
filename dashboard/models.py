from django.db import models

class FarmData(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=100)

    # Weather
    air_temperature_c = models.FloatField()
    relative_humidity = models.FloatField()
    rainfall_mm = models.FloatField()
    wind_speed_mps = models.FloatField(default=0)
    solar_radiation_wm2 = models.FloatField(default=0)

    # Soil
    soil_moisture = models.FloatField()
    soil_temperature_c = models.FloatField(default=0)
    soil_ph = models.FloatField()

    # Crop
    growth_stage = models.CharField(max_length=50, default="")
    crop_health_index = models.IntegerField()
    crop_duration_days = models.IntegerField(default=120)

    # Farm status
    irrigation_status = models.CharField(max_length=10, default="OFF")
    fertilizer_applied = models.CharField(max_length=50, default="NONE")
    pest_risk_level = models.CharField(max_length=10, default="LOW")

    region = models.CharField(max_length=50)
    datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.state} - {self.city} - {self.crop_type}"
