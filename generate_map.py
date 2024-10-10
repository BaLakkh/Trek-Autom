import requests
import folium
from datetime import datetime
import pytz

spreadsheet_id = '1KLmYkv_-xfwzWcDT0AximnUGAn7E5u_NSltj77GLa2c'
range_name = 'Lat_Lon!A1:C1000'
api_key = 'AIzaSyBHlI-BiN0I1ZgpGFsiEKHNX3rx8AjTKcY'

# Construisez l'URL pour récupérer les données depuis Google Sheets
url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}?key={api_key}'

response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
    except ValueError as e:
        print("Erreur lors de la conversion en JSON:", e)
else:
    print(f"Erreur HTTP {response.status_code}: {response.reason}")

rows = data.get('values', [])

# Obtenir l'heure actuelle
paris_tz = pytz.timezone('Europe/Paris')
current_time = datetime.now(paris_tz).strftime('%Y-%m-%d %H:%M:%S')

# Créer la carte
m = folium.Map(location=[56.819817, -5.105218], zoom_start=8.4)

# Ajouter des marqueurs pour chaque point de votre Google Sheets
for row in rows[1:]:
    folium.Marker(location=[float(row[1]), float(row[2])], popup=row[0]).add_to(m)

# Ajouter l'heure de génération en tant que Custom Control
title_html = f'''
    <div style="position: fixed; 
                bottom: 50px; left: 50px; width: 300px; height: 40px; 
                background-color: white; z-index:9999;
                font-size:14px; border:2px solid grey; padding: 10px;">
        Carte générée à : {current_time}
    </div>
    '''

m.get_root().html.add_child(folium.Element(title_html))

# Charger le fichier GeoJSON du GR10
geojson_file_west_highland_way = 'west_highland_way.geojson'  # Remplacez par le chemin de votre fichier GeoJSON
geojson_file_skye = 'skye_trail__scotland_.geojson'

folium.GeoJson(geojson_file_west_highland_way, name="West Highland Way").add_to(m)
folium.GeoJson(geojson_file_skye, name="Skye Trail").add_to(m)

# Ajouter un contrôle de couches
folium.LayerControl().add_to(m)

# Sauvegarder la carte
m.save('carte.html')
