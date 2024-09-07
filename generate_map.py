import gspread
from oauth2client.service_account import ServiceAccountCredentials
import folium

# Charger les informations d'identification
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('autom-gr10-556ec077cf0d.json', scope)
client = gspread.authorize(creds)

# Accéder à la feuille Google Sheets
sheet = client.open("LATLON GR10").sheet1

# Récupérer toutes les données
rows = sheet.get_all_records()

# Générer la carte
m = folium.Map(location=[42.5, 1.5], zoom_start=10)

# Ajouter des marqueurs pour chaque point
for row in rows:
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['Timestamp']).add_to(m)

# Sauvegarder la carte dans un fichier HTML
m.save('carte.html')
