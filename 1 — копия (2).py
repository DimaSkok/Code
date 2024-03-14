from skyfield.api import EarthSatellite, load
import math

R = 6356.7523
pi = 3.141592653589793

data = load('de421.bsp')
line1 = "1 33591U 09005A   22256.82151620  .00000034  00000-0  20523-4 0 9999"
line2 = "2 33591 099.0678 182.1456 0014237 307.7083   .2897 14.12431814670202"
satellite = EarthSatellite(line1, line2, name='SAT')

ts = load.timescale()

# Координаты антенны (в данном случае примерные значения)
antenna_lat = math.radians(37.7749) # Широта Сан-Франциско
antenna_lon = math.radians(-122.4194) # Долгота Сан-Франциско
antenna_alt_km = 0.1 # Высота антенны над уровнем моря в км

# Создаем список всех возможных комбинаций времени
times_list = []
for day in range(29,30):
    for hour in range(17,24):
        for minute in range(60):
            times_list.append(ts.utc(2024, 2, day, hour, minute))

for day in range(1):
    for hour in range(18):
        for minute in range(48):
            times_list.append(ts.utc(2024, 3, day+1, hour, minute))

# Итерируем по всем комбинациям времени
for t in times_list:
    geocentric = satellite.at(t)
    subpoint = geocentric.subpoint()

    shir_sat = subpoint.latitude.radians
    dol_sat = subpoint.longitude.radians
    h_sat = subpoint.elevation.km

    x_sat = (h_sat + R) * math.cos(shir_sat) * math.cos(dol_sat)
    y_sat = (h_sat + R) * math.cos(shir_sat) * math.sin(dol_sat)
    z_sat= (h_sat + R) * math.sin(shir_sat)

    x_antenna= (antenna_alt_km + R) * math.cos(antenna_lat) * math.cos(antenna_lon)
    y_antenna= (antenna_alt_km + R) * math.cos(antenna_lat) * math.sin(antenna_lon)
    z_antenna= (antenna_alt_km + R) * math.sin(antenna_lat)


    dx = x_sat - x_antenna
    dy = y_sat - y_antenna
    dz = z_sat - z_antenna

    az = math.atan2(dy, dx)
    el = math.atan2(dz, math.sqrt(dx*dx + dy*dy))

    az_deg = math.degrees(az)
    el_deg = math.degrees(el)

    print(f"At time {t.utc_strftime('%Y-%m-%d %H:%M:%S')}:")
    print(f"Azimuth: {az_deg} degrees")
    print(f"Elevation: {el_deg} degrees")