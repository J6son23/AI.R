import requests

def get_transit_directions(origin, destination, api_key):
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": "transit",
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Example usage:
origin = "Starting Point"
destination = "Destination"
api_key = "YOUR_API_KEY"

directions_data = get_transit_directions(origin, destination, api_key)
print(directions_data)
