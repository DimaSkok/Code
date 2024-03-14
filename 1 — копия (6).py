from skyfield.api import Loader, Topos
from skyfield.api import EarthSatellite

load = Loader('~/skyfield-data')
ts = load.timescale()
planets = load('de421.bsp')
earth = planets['earth']

antenna_lat = 55.9300670
antenna_lon = 37.5180770
antenna_location = Topos(antenna_lat, antenna_lon)

line1 = "1 33591U 09005A   24066.55361099  .00000265  00000-0  16698-3 0 9997"
line2 = "2 33591 99.0617 121.2122 0013345 218.2874 141.7351 14.12940546776877"

satellite = EarthSatellite(line1, line2)

start_time = ts.utc(2024, 2, 29, 18, 0, 0)
end_time = ts.utc(2024, 3, 1, 18, 0, 0)

times, events = satellite.find_events(antenna_location, start_time, end_time,
                                      altitude_degrees=10.0)

print('Прогноз видимости аппарата для антенны-наблюдателя:')
print('-----------------------------------------------------')
print('|    Время начала    |     Время окончания    |')
print('-----------------------------------------------------')

for ti_start, ti_end in zip(times[::2], times[1::2]):
    print(f'| {ti_start.utc_iso()} | {ti_end.utc_iso()} |')

    # Вычисление углов только для времени видимости спутника
    geocentric_start = satellite.at(ti_start)
    subpoint_start = geocentric_start.subpoint()

    shir_sat_start = subpoint_start.latitude.radians
    dol_sat_start = subpoint_start.longitude.radians
    h_sat_start = subpoint_start.elevation.km

    x_sat_start = (h_sat_start + earth.radius.km) * math.cos(shir_sat_start) * math.cos(dol_sat_start)
    y_sat_start = (h_sat_start + earth.radius.km) * math.cos(shir_sat_start) * math.sin(dol_sat_start)
    z_sat_start = (h_sat_start + earth.radius.km) * math.sin(shir_sat_start)

    x_antenna = (earth.radius.km + antenna_location.elevation.m) * math.cos(math.radians(antenna_lat)) * math.cos(
        math.radians(antenna_lon))
    y_antenna = (earth.radius.km + antenna_location.elevation.m) * math.cos(math.radians(antenna_lat)) * math.sin(
        math.radians(antenna_lon))
    z_antenna = (earth.radius.km + antenna_location.elevation.m) * math.sin(math.radians(antenna_lat))

    dx = x_sat_start - x_antenna
    dy = y_sat_start - y_antenna
    dz = z_sat_start - z_antenna

    azimuth = math.degrees(math.atan2(dy, dx))

    elevation = math.degrees(math.asin(dz / math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)))

    print(f'| Угол азимута: {azimuth:.2f} градусов | Угол места: {elevation:.2f} градусов |')

print('-----------------------------------------------------')