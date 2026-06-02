from django.db import models

class FarmData(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=100)

    air_temperature_c = models.FloatField()
    relative_humidity = models.FloatField()

    rainfall_mm = models.FloatField()

    soil_moisture = models.FloatField()
    soil_ph = models.FloatField()

    crop_health_index = models.IntegerField()

    region = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.state} - {self.city}"