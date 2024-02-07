import requests

url = 'http://13.53.130.43:8080/teachers'
headers = {'Content-Type': 'application/json'}
data = {}  # Your Flask app doesn't use this, but it's here to simulate a typical JSON POST request

response = requests.post(url, json=data, headers=headers)
print(response.json())
