import pyproj

def utm_to_latlon(zone_number, zone_letter, easting, northing):
    south = zone_letter in ['C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M']
    
    utm_proj = pyproj.Proj(proj='utm', zone=zone_number, south=south, ellps='WGS84')
    latlon_proj = pyproj.Proj(proj='latlong', datum='WGS84')
    lat, lon = pyproj.transform(utm_proj, latlon_proj, easting, northing)
    
    return lat, lon

# Datos de ejemplo
zone_number = 18
zone_letter = 'G'
easting = 612679.972693128
northing = 5228107.06744415

lat, lon = utm_to_latlon(zone_number, zone_letter, easting, northing)
print(f', Longitud: {lon}, Latitud: {lat}')
