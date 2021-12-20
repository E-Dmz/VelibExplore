import folium
from velib.data import Velib

class StationMap:
    def __init__(self):
        self.map = folium.Map(location=[48.85, 2.35], zoom_start=13)
        self.df = Velib().get_stations_df()
        self.df['stationCode'] = self.df['stationCode'].astype(int)

    def marker(self, *stationCodes: int, color = "green", icon = 'bicycle'):
        for stationCode in stationCodes:
            row = self.df.query(f"stationCode == {stationCode}")
            location = [row.lat.values[0], row.lon.values[0]]
            popup = row.name.values[0]
            marker = folium.Marker(location=location,
                                popup=popup,
                                icon=folium.Icon(color=color,icon= icon))
            marker.add_to(self.map)

    def show(self):
        return self.map
