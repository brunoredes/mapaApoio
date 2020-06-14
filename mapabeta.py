import folium
import pandas

data = pandas.read_csv("dadosapoiopretobeta1.txt")
lat = list(data["Norte"])
lon = list(data["Leste"])
elev = list(data["Sobre"])
name = list(data["Projeto"])
insta = list(data["instagram"])
acts = list(data["acoes"])
 
def color_producer(action):
    if action == 'alimentacao':
         return 'orange'
    elif action == 'arrecadacao':
         return 'red'
    elif action == 'educacao':
         return 'blue'
    elif action == 'saude':
         return 'gray'
    elif action == 'lgbt':
         return 'purple'
    elif action == 'arte':
         return 'black'  
    else:
        return 'green'  

html = """
Projeto:<br>
<a href="https://www.instagram.com/%s" target="_blank">%s </a> <br>
O que faz: %s 
"""
 
map = folium.Map(location=[-23.55,-46.64], zoom_start=10, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, ig, name, el, act in zip(lat, lon, insta, name, elev, acts):
    iframe = folium.IFrame(html=html % (ig, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(act))))
 
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Mapabeta.html")
