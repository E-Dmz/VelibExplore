import pandas as pd
import requests

URL_VELIB_STATUS = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"
URL_VELIB_STATIONS = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"

class Velib:

    def get_velib_df(self):
        response = requests.get(URL_VELIB_STATUS)
        velib_df = pd.DataFrame(response.json()["data"]["stations"])
        return velib_df

    def get_stations_df(self):
        response = requests.get(URL_VELIB_STATIONS)
        stations_df = pd.DataFrame(response.json()["data"]["stations"])
        return stations_df
