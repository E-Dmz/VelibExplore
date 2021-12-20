import sys
import requests
import pandas as pd
import datetime as dt
import numpy as np

URL_VELIB_STATUS = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"
def get_velib_df():
    response = requests.get(URL_VELIB_STATUS)
    velib_df = (pd.DataFrame(response.json()["data"]["stations"])
                    .set_index("stationCode"))
    return velib_df

velib_df = get_velib_df()

velib_df.reset_index(inplace = True)
find_mecha = lambda row: row['num_bikes_available_types'][0].get('mechanical', np.nan)
find_elec = lambda row: row['num_bikes_available_types'][1].get('ebike', np.nan)
velib_df['meca'] = velib_df.apply(find_mecha, axis = 1)
velib_df['elec'] = velib_df.apply(find_elec, axis = 1)
velib_df['park'] = velib_df['num_docks_available']
velib_df['datetime'] = dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H%M')
velib_df = velib_df[['datetime', 'stationCode', 'meca', 'elec', 'park']]

#velib_df.iloc[0:0,:].to_csv("test.csv", index = False)

velib_df.to_csv('/Script/VelibScrap/test-15-1.csv', mode='a', header=False, index = False)
