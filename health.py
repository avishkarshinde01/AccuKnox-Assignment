import requests

URL = "http://example.com"  # Replace with your app URL

try:
    response = requests.get(URL, timeout=5)
    if response.status_code == 200:
        print("Application is UP!")
    else:
        print(f"Application is DOWN! Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Application is DOWN! Error: {e}")
