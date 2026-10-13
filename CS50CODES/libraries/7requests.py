#APIs
#JSON no funciona
import requests
import sys
import json

if len(sys.argv) !=2:
    sys.exit()
    
response= requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
diccionario_artist = response.json()
print(json.dumps(diccionario_artist, indent= 2))
for results in diccionario_artist["results"]:
    print(results['trackName'], results['collectionName'], results['artistName'])
# python 7requests.py feid, imprime las primeras 10 canciones
