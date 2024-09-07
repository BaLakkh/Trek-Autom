import requests
import folium

# Remplacez YOUR_SHEET_ID par l'ID de votre Google Sheet
url = 'https://spreadsheets.google.com/feeds/list/1KLmYkv_-xfwzWcDT0AximnUGAn7E5u_NSltj77GLa2c/od6/public/values?alt=json'

# Faire une requête HTTP pour récupérer les données
response = requests.get(url)
data = response.json()

# Extraire les données
rows = data['feed']['entry']

# Créer la carte
m = folium.Map(location=[42.5, 1.5], zoom_start=10)

# Ajouter des marqueurs à la carte pour chaque entrée
for row in rows:
    latitude = float(row['gsx$latitude']['$t'])
    longitude = float(row['gsx$longitude']['$t'])
    timestamp = row['gsx$timestamp']['$t']
    folium.Marker(location=[latitude, longitude], popup=timestamp).add_to(m)

# Sauvegarder la carte
m.save('carte.html')
