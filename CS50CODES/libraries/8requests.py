import requests

def main():
    print("Que artista quieres:")
    artist = input()
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search", {"q": artist})
        response.raise_for_status() #sirve para que salga el except si no funciona
    except requests.HTTPError:
        print("No se pudo completar la API")
        return
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork["title"]}")
    
main()