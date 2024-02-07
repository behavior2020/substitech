import requests

# URL for the POST request
url1 = 'http://13.53.130.43:8080/releventsubstitutes'
# Data and headers for the POST request
data = {}  # Assuming your endpoint expects JSON data
headers = {'Content-Type': 'application/json'}

# Making the POST request to /teachers
response1 = requests.post(url1, json=data, headers=headers)
print(response1.json())

# URL for the GET request
url2 = 'http://13.53.130.43:8080/connected'

# Making the GET request to /datascience
response2 = requests.get(url2)
print(response2.text)
