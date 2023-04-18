import tqdm
from dashboard.models import BikeTrip
import pandas as pd

#python manage.py runscript load_data
def run():
    data_df = pd.read_csv('../london_merged.csv')
    # next(reader)  # Advance past the header

    BikeTrip.objects.all().delete()

    loader = tqdm.tqdm(data_df.itertuples(index=False), desc='Loading data...', leave=False, total=data_df.shape[0])
    for row in loader:
        # print(row)
        
        trip = BikeTrip(
            timestamp=row.timestamp, 
            count_bike_shares=row.cnt, 
            real_temp=row.t1, 
            feel_temp=row.t2, 
            humidity=row.hum, 
            wind_speed=row.wind_speed, 
            weather_code=row.weather_code, 
            is_holiday=row.is_holiday, 
            is_weekend=row.is_weekend, 
            season=row.season 
        )
        trip.save()

    print('Data loaded!')