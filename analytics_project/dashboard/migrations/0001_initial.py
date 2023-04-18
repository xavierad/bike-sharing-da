# Generated by Django 4.2 on 2023-04-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=20)),
                ('count_bike_shares', models.CharField(max_length=10)),
                ('real_temp', models.CharField(max_length=10)),
                ('feel_temp', models.CharField(max_length=10)),
                ('humidity', models.CharField(max_length=10)),
                ('wind_speed', models.CharField(max_length=10)),
                ('weather_code', models.CharField(max_length=10)),
                ('is_holiday', models.CharField(max_length=2)),
                ('is_weekend', models.CharField(max_length=2)),
                ('season', models.CharField(max_length=10)),
            ],
        ),
    ]