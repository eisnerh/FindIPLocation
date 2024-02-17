import json
import webbrowser
from urllib.request import urlopen


# Function to get public IP address
def get_public_ip():
    """
    Obtiene la dirección IP pública del dispositivo.

    Returns:
        str: La dirección IP pública del dispositivo.
    """
    response_my_ip = urlopen('https://api.ipify.org?format=json')
    data = json.load(response_my_ip)
    return data['ip']


# Get the public IP address
public_ip = get_public_ip()
print("Your public IP address:", public_ip)

# Fetch IP information from IP-API.com
url: str = f"http://ip-api.com/json/{public_ip}"
response = urlopen(url)
ip_info = json.load(response)

# Obtener la latitud y longitud
newLatitude = ip_info['lat']
newLongitude = ip_info['lon']

# Mostrar la latitud y longitud
print("Latitude:", newLatitude)
print("Longitude:", newLongitude)


# Abrir el mapa en una nueva ventana del navegador
def open_map(lat, lon):
    url_google_maps = f'https://www.google.com/maps/search/?api=1&query={lat},{lon}'
    webbrowser.open(url_google_maps)


open_map(newLatitude, newLongitude)
