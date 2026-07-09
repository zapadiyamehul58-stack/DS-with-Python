import requests

url = "https://mocki.io/v1/60d3ee1b-5a00-45ad-bddb-95a5344e2936"
response = requests.get(url)

print(response.json())
