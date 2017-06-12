import googlemaps
import folium
gmaps = googlemaps.Client(key = 'AIzaSyA8hI7fOaEjgt7hFD5QIKgbA3nQdgBJj0o')
geo = gmaps.geocode('Vancouver Burrard Station')
print(geo)
