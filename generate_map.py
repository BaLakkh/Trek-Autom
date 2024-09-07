import requests
import folium

spreadsheet_id = '1KLmYkv_-xfwzWcDT0AximnUGAn7E5u_NSltj77GLa2c'
range_name = 'Lat_Lon!A1:C1000'  # Plage spécifique
api_key = 'AIzaSyBHlI-BiN0I1ZgpGFsiEKHNX3rx8AjTKcY'

# Construisez l'URL
url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}?key={api_key}'

# Faire une requête HTTP pour récupérer les données
response = requests.get(url)

response = requests.get(url)

# Vérifier si la requête a réussi (code 200)
if response.status_code == 200:
    try:
        data = response.json()  # Tenter de lire le JSON
    except ValueError as e:
        print("Erreur lors de la conversion en JSON:", e)
else:
    print(f"Erreur HTTP {response.status_code}: {response.reason}")

# Extraire les données
rows = data.get('values', [])
print(rows)


# Créer la carte
m = folium.Map(location=[42.5, 1.5], zoom_start=10)

# Ajouter des marqueurs à la carte pour chaque entrée
# Ajouter des marqueurs pour chaque point
for row in rows[1:]:
    folium.Marker(location=[row[1], row[2]], popup=row[0]).add_to(m)

# Sauvegarder la carte
m.save('carte.html')
