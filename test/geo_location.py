import requests

def get_geo_location(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        if data["status"] == "success":
            return data.get("country", "Unknown")

    except Exception as e:
        print(f"geolocation error: {e}")

    return "Unknown"