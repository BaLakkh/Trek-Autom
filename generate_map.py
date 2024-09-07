import requests
import folium

# Remplacez YOUR_SHEET_ID par l'ID de votre Google Sheet
url = 'https://spreadsheets.google.com/feeds/list/1KLmYkv_-xfwzWcDT0AximnUGAn7E5u_NSltj77GLa2c/od6/public/values?alt=json'

# Faire une requête HTTP pour récupérer les données
response = requests.get(url)

response = requests.get(url)

# Vérifier si la requête a réussi (code 200)
if response.status_code == 200:
    print("Requête réussie!")
    print("Contenu de la réponse :")
    print(response.text)  # Afficher le contenu brut de la réponse
    try:
        data = response.json()  # Tenter de lire le JSON
        print("Données JSON :")
        print(data)
    except ValueError as e:
        print("Erreur lors de la conversion en JSON:", e)
else:
    print(f"Erreur HTTP {response.status_code}: {response.reason}")

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
