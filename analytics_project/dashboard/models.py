from django.db import models

# Create your models here.
class BikeTrip(models.Model):
    timestamp: str = models.CharField(max_length=30)
    count_bike_shares: str = models.CharField(max_length=10)
    real_temp: str = models.CharField(max_length=10)
    feel_temp: str = models.CharField(max_length=10)
    humidity: str = models.CharField(max_length=10)
    wind_speed: str = models.CharField(max_length=10)
    weather_code: str = models.CharField(max_length=10)
    is_holiday: str = models.CharField(max_length=2)
    is_weekend: str = models.CharField(max_length=2)
    season: str = models.CharField(max_length=10)
    